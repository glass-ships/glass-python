#########################################################################################
##   This script manually sets environment variables set by $ROOTSYS/bin/thisroot.sh   ##
##   Mainly as a way of avoiding conflicts between user pythons and python used to     ##
##   compile ROOT from source. ROOT is now packaged in conda - I recommend factoring   ##
##   your code to be compatible with conda ROOT.                                       ##
#########################################################################################

# added by thisroot.sh
export ROOTSYS=/packages/root6.12
export DYLD_LIBRARY_PATH=$ROOTSYS/lib
export JUPYTER_PATH=$ROOTSYS/etc/notebook
export LIBPATH=$ROOTSYS/lib
export ROOTSYS=$ROOTSYS
export SHLIB_PATH=$ROOTSYS/lib

# appended to by thisroot.sh
export LD_LIBRARY_PATH=$ROOTSYS/lib:$LD_LIBRARY_PATH
export MANPATH=$ROOTSYS/man:$MANPATH
export PATH=$ROOTSYS/bin:$PATH
export PYTHONPATH=$ROOTSYS/lib:$PYTHONPATH