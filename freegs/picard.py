"""
Routines for solving the nonlinear part of the Grad-Shafranov equation
"""

from numpy import amin, amax

def solve(eq, profiles, constrain=None, rtol=1e-3, blend=0.0,
          show=False, axis=None, pause=0.0001, 
          niter=2, sublevels=4, ncycle=2):
    """
    Perform Picard iteration to find solution to the Grad-Shafranov equation
    
    eq       - an Equilibrium object (equilibrium.py)
    profiles - A Profile object for toroidal current (jtor.py)

    rtol     - Relative tolerance (change in psi)/( max(psi) - min(psi) )
    blend    - Blending of previous and next psi solution
               psi{n+1} <- psi{n+1} * (1-blend) + blend * psi{n}

    show     - If true, plot the plasma equilibrium at each nonlinear step
    axis     - Specify a figure to plot onto. Default (None) creates a new figure
    pause    - Delay between output plots. If negative, waits for window to be closed
    
    The linear solve is controlled by the following parameters:
    
    niter     - Number of Jacobi iterations per level
    sublevels - Number of levels in the multigrid
    ncycle    - Number of V-cycles
    """
    
    if constrain is not None:
        # Set the coil currents to get X-points in desired locations
        constrain(eq)
    
    # Get the total psi = plasma + coils
    psi = eq.psi()
    
    if show:
        import matplotlib.pyplot as plt
        from plotting import plotEquilibrium
        import critical
        
        if pause > 0. and axis is None:
            # No axis specified, so create a new figure
            fig = plt.figure()
            axis = fig.add_subplot(111)
        
    # Start main loop
    while True:
        if show:
            # Plot state of plasma equilibrium
            if pause < 0:
                fig = plt.figure()
                axis = fig.add_subplot(111)
            else:
                axis.clear()
            
            plotEquilibrium(eq,axis=axis,show=False)
            
            if pause < 0:
                # Wait for user to close the window
                plt.show()
            else:
                # Update the canvas and pause
                # Note, a short pause is needed to force drawing update
                axis.figure.canvas.draw()
                plt.pause(pause) 
        
        # Copy psi to compare at the end
        psi_last = psi.copy()
        
        # Solve equilbrium
        eq.solve(profiles, niter=niter, sublevels=sublevels, ncycle=ncycle)
        
        # Get the new psi, including coils
        psi = eq.psi()
    
        # Compare against last solution
        psi_last -= psi 
        psi_maxchange = amax(abs(psi_last))
        psi_relchange = psi_maxchange/(amax(psi) - amin(psi))
        
        print("Maximum change in psi: %e. Relative: %e" % (psi_maxchange, psi_relchange))
        
        # Check if the relative change in psi is small enough
        if psi_relchange < rtol:
            break
        
        # Adjust the coil currents
        if constrain is not None:
            constrain(eq)
        
        psi = (1. - blend)*eq.psi() + blend*psi_last
        
        