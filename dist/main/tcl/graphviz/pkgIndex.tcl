package ifneeded Tcldot 8.0.5 "
	load [file join $dir libtcldot.so] Tcldot"
package ifneeded Tclpathplan 8.0.5 "
	load [file join $dir libtclplan.so] Tclpathplan"
package ifneeded Gdtclft 8.0.5 "
	load [file join $dir libgdtclft.so] Gdtclft"
package ifneeded gv 0 "
	load [file join $dir libgv_tcl.so] gv"
# end
