#!/gnuplot
#
#    
#    	G N U P L O T
#    	Version 5.0 patchlevel 0    last modified 2015-01-01 
#    
#    	Copyright (C) 1986-1993, 1998, 2004, 2007-2015
#    	Thomas Williams, Colin Kelley and many others
#    
#    	gnuplot home:     http://www.gnuplot.info
#    	faq, bugs, etc:   type "help FAQ"
#    	immediate help:   type "help"  (plot window: hit 'h')
# set terminal wxt 0 enhanced
# set output
unset clip points
set clip one
unset clip two
set bar 1.000000 front
set border 31 front lt black linewidth 1.000 dashtype solid
set zdata 
set ydata 
set xdata 
set y2data 
set x2data 
set boxwidth
set style fill  empty border
set style rectangle back fc  bgnd fillstyle   solid 1.00 border lt -1
set style circle radius graph 0.02, first 0.00000, 0.00000 
set style ellipse size graph 0.05, 0.03, first 0.00000 angle 0 units xy
set dummy x, y
set format x "10^{%L}"
#set format y "10^{%L}"
set format y "%g"
set format x2 "% h" 
set format y2 "% h" 
set format z "% h" 
set format cb "% h" 
set format r "% h" 
set timefmt "%d/%m/%y,%H:%M"
set angles radians
unset grid
set raxis
set style parallel front  lt black linewidth 2.000 dashtype solid
set key title ""
set key inside left top vertical Right noreverse enhanced autotitle nobox
set key noinvert samplen 4 spacing 1 width 0 height 0 
set key maxcolumns 0 maxrows 0
set key noopaque
unset label
unset arrow
set style increment default
unset style line
unset style arrow
set style histogram clustered gap 2 title textcolor lt -1
unset object
set style textbox transparent margins  1.0,  1.0 border
unset logscale
set logscale y
#set logscale x
set offsets 0, 0, 0, 0
set pointsize 1
set pointintervalbox 1
set encoding default
unset polar
unset parametric
unset decimalsign
set view 60, 30, 1, 1
set samples 100, 100
set isosamples 10, 10
set surface 
unset contour
set cntrlabel  format '%8.3g' font '' start 5 interval 20
set mapping cartesian
set datafile separator "	"
unset hidden3d
set cntrparam order 4
set cntrparam linear
set cntrparam levels auto 5
set cntrparam points 5
set size ratio 0 1,1
set origin 0,0
set style data points
set style function lines
unset xzeroaxis
unset yzeroaxis
unset zzeroaxis
unset x2zeroaxis
unset y2zeroaxis
#set ticslevel 0.5
#set tics scale  1, 0.5, 1, 1, 1
set mxtics default
set mytics default
set mztics default
set mx2tics default
set my2tics default
set mcbtics default
set mrtics default
set xtics border in scale 1,0.5 mirror norotate  autojustify
#set xtics 10000
set xtics autofreq  norangelimit
set ytics border in scale 1,0.5 mirror norotate  autojustify
set ytics autofreq  norangelimit
set ztics border in scale 1,0.5 nomirror norotate  autojustify
set ztics autofreq  norangelimit
unset x2tics
unset y2tics
set cbtics border in scale 1,0.5 mirror norotate  autojustify
set cbtics autofreq  norangelimit
set rtics axis in scale 1,0.5 nomirror norotate  autojustify
set rtics autofreq  norangelimit
unset paxis 1 tics
unset paxis 2 tics
unset paxis 3 tics
unset paxis 4 tics
unset paxis 5 tics
unset paxis 6 tics
unset paxis 7 tics
set title "" 
set title  font "" norotate
set timestamp bottom 
set timestamp "" 
set timestamp  font "" norotate
set rrange [ * : * ] noreverse nowriteback
set trange [ * : * ] noreverse nowriteback
set urange [ * : * ] noreverse nowriteback
set vrange [ * : * ] noreverse nowriteback
set xlabel "{/Symbol D}Size (Bytes)" 
set xlabel  font "" textcolor lt -1 norotate
set x2label "" 
set x2label  font "" textcolor lt -1 norotate
set xrange [ * : * ] noreverse nowriteback
set x2range [ * : * ] noreverse nowriteback
set ylabel "Probability Density (%)" 
set ylabel  font "" textcolor lt -1 rotate by -270
set y2label "" 
set y2label  font "" textcolor lt -1 rotate by -270
set yrange [ * : * ] noreverse nowriteback
set y2range [ * : * ] noreverse nowriteback
set zlabel "" 
set zlabel  font "" textcolor lt -1 norotate
set zrange [ * : * ] noreverse nowriteback
set cblabel "" 
set cblabel  font "" textcolor lt -1 rotate by -270
set cbrange [ * : * ] noreverse nowriteback
set paxis 1 range [ * : * ] noreverse nowriteback
set paxis 2 range [ * : * ] noreverse nowriteback
set paxis 3 range [ * : * ] noreverse nowriteback
set paxis 4 range [ * : * ] noreverse nowriteback
set paxis 5 range [ * : * ] noreverse nowriteback
set paxis 6 range [ * : * ] noreverse nowriteback
set paxis 7 range [ * : * ] noreverse nowriteback
set zero 1e-008
set lmargin  8
set bmargin  3
set rmargin  3
set tmargin  1
set locale "Korean_Korea.949"
set pm3d explicit at s
set pm3d scansautomatic
set pm3d interpolate 1,1 flush begin noftriangles noborder corners2color mean
set palette positive nops_allcF maxcolors 0 gamma 1.5 color model RGB 
set palette rgbformulae 7, 5, 15
set colorbox default
set style boxplot candles range  1.50 outliers pt 7 separation 1 labels auto unsorted
set loadpath 
set fontpath 
set psdir
set fit brief errorvariables nocovariancevariables errorscaling prescale nowrap v5
GNUTERM = "wxt"
ARGC = 0
ARG0 = ""
x = 0.0
##PLOT!
set term pdfcairo dashed enhanced color size 6.75, 2 font "Helvetica, 14" 
#set term pngcairo enhanced color size 800,600 font "Helvetica, 14" 
set log x
unset log y

set size 0.33,1
set key bottom center
set key font "Helvetica, 8"
set o './FIG_003_from0.pdf'
set multiplot
set ytic 0.1

set origin 0,0
set xrange [7e03:1e08]
set xtic (1e04,1e05,1e06,1e07,1e08)
set yrange [0:0.7]
set xlabel "{/Helvetica-Italic N_e}" offset 0,0.2,0
set ylabel "{/Helvetica Shorterm revisit fraction}" offset -0.5,0,0
set label 1 "{/Helvetica-Bold a}" at screen 0.01,0.98
pl './data/replaced_editors_per_10000_edits_all.txt' u 1:3 title "10%" ps 0.5, '' u 1:7 title "30%" ps 0.5, '' u 1:11 title "50%" ps 0.5, '' u 1:15 title "70%" ps 0.5, '' u 1:19 title "90%" ps 0.5
unset label

set key bottom right
set origin 0.33,0
set xrange [7e03:1e08]
set xtic (1e04,1e05,1e06,1e07,1e08)
set yrange [0.0:1.1]
set xlabel "{/Helvetica-Italic N_e}" offset 0,0.2,0
set ylabel "{/Helvetica Longterm revisit fraction}" offset -0.5,0,0
set label 2 "{/Helvetica-Bold b}" at screen 0.34,0.98
pl './data/replaced_editors_per_10000_edits_all_accumulated.txt' u 1:3 title "10%" ps 0.5, '' u 1:7 title "30%" ps 0.5, '' u 1:11 title "50%" ps 0.5, '' u 1:15 title "70%" ps 0.5, '' u 1:19 title "90%" ps 0.5
unset label


set lmargin  5
set bmargin  1.69
set rmargin  3
set tmargin  -0.2
unset key
set size 0.33, 1.18
set origin 0.66,0
set xlabel "{/Helvetica-Italic N_e} ({/Symbol \264}10^7)" offset 0,0.8,0
set ylabel "Correlation length ({/Symbol \264}10^4)" offset -1,0,0
unset log x
unset log y
unset format x
unset format y
set xtic 10000000 offset 0,0.4,0 font "Helvetica, 14"
set ytic 20000 font "Helvetica, 14"
set xrange [00000:4e07]
set yrange [0:97000]
set format x "%.0l"
set format y "%.0l"
set label 3 "{/Helvetica-Bold c}" at screen 0.67,0.98
set auto cb
set palette define (-1 0.094118 0.25098 0.521569, -0.4 0.17835 0.5 0.7, 0 0.262745 0.752941 0.878431, 0.3 0.47451 0.709804 0.12549, 0.4 0.968627 0.886275 0.278431, 1 0.854902 0.086275 0.133333)
set cbtic 0.1
set pm3d map
spl './data/editor_editnum_correlation_before_after.txt' u ($1-10000):($2-1000):3
unset label

unset multiplot
unset o
#EOF