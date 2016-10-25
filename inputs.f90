!! This is an inputs file for WFCode
!! Must be in right order until I sort out a Makefile
	'test.dat' ! output file name
	2000 ! nk number of k points, log spaced
	0.001 ! kmin
	1.e3 ! kmax
	31 ! nz number of z points, lin spaced
	3. ! zmin
	6. ! zmax
	0  ! imead
	0  ! iwdm
	1  ! ifdm
	1  ! ibarrier
	1  ! iconc
	1  ! iprofile