Modifications to HMCode by David Marsh:

* Simple: modify just the power

Added FDM and WDM transfer functions.
Added option ifdm and iwdm to include them.

* Complicated: add a mass dependent barrier

Added option ibarrier to do this.
Added two functions, benson and marsh for the modified barriers.
Benson is correct. Marsh one is a fudge for now
Use barrier function to create new look up table nuST which is the modified barrier. 
change mmin=1.e6, as otherwise you get NaNs way below the MF cut off

NOTE: The modified barrier is *only* passed into the ST mass function in the integrand. Otherwise you get an extra term appearing which makes the one halo term negative at large k, which is inconsistent (it is the logarithmic derivative of \delta, which is large and negative at low M). Including only in ST is consistent with the definitions in Marsh and Silk. Check on Benson. 

This all matters because integrals are converted to \nu space by Mead, which makes certain assumptions. What we really want to do is do the integral in \sigma space. I think this is consistent with the principles of PS when the barrier depends on mass, and consistent with all Mead’s changes of variables. You use the variance at z=0 to define the mass, and ask how this compares to a moving barrier, even if the barrier has mass dependence. See also subhalo notes on measures.


* More complicated: change halo density profiles and concentration

Haven’t started on this yet.