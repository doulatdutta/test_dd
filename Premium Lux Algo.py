// This work is licensed under a Attribution-NonCommercial-ShareAlike 4.
0International (CC BY-NC-SA 4.0) https://creativecommons.org/licenses/by-nc-sa/4.0/// © LuxAlgo

//@version=5indicator("Premium Lux Algo", overlay=true, precision=0, explicit_plot_zorder=true,max_labels_count=500)

// Get user inputsensitivity = input.float(5.5, "Sensitivity (0.5 - 12)", 0.5, 12, step=0.05, group= 'Settings')

ShowSmartTrail = input.bool(true, 'Smart Trail ', inline = 'overlayLine1',group = 'Settings')maj = input(true, title='TP Points', inline = 'overlayLine1', group = 'Settings')

enableReversal = input.bool(false, 'Reversal Signal ', inline ='overlayLine2', group = 'Settings')show_ha = input.bool(false, 'Trend Tracker', inline = 'overlayLine2', group ='Settings')

enableSR = input(false, 'Support/Resistance ', inline = 'overlayLine3', group= 'Settings')usePsar = input.bool(false, 'PSAR', inline = 'overlayLine3', group ='Settings')

show_rev = input.bool(true, 'Reversal Cloud ', inline = 'overlayLine4', group= 'Settings')Show_rangefilter = input.bool(true, 'Range Filter', inline = 'overlayLine4', group= 'Settings')

Show_SuperIchi = input.bool(true, 'SuperIchi ', inline = 'overlayLine5',group = 'Settings')Show_TBO = input.bool(true, 'Show TBO', inline = 'overlayLine5', group ='Settings')

// Functionssupertrend(_src, factor, atrLen) => atrat = ta.atr(atrLen) upperBand = _src + factor * atrat lowerBand = _src - factor * atrat prevLowerBand = nz(lowerBand[1]) prevUpperBand = nz(upperBand[1]) lowerBand := lowerBand > prevLowerBand or close[1] < prevLowerBand ?lowerBand : prevLowerBand upperBand := upperBand < prevUpperBand or close[1] > prevUpperBand ?upperBand : prevUpperBand int direction = na float superTrend = na prevSuperTrend = superTrend[1] if na(atrat[1]) direction := 1 else if prevSuperTrend == prevUpperBand direction := close > upperBand ? -1 : 1 else direction := close < lowerBand ? 1 : -1 superTrend := direction == -1 ? lowerBand : upperBand [superTrend, direction]// Get ComponentsocAvg = math.avg(open, close)ema1 = ta.ema(high, 9)ema2 = ta.ema(high, 12)ema3 = ta.ema(high, 15)ema4 = ta.ema(high, 18)sma1 = ta.sma(close, 5)sma2 = ta.sma(close, 6)sma3 = ta.sma(close, 7)sma4 = ta.sma(close, 8)sma5 = ta.sma(close, 9)sma6 = ta.sma(close, 10)sma7 = ta.sma(close, 11)sma8 = ta.sma(close, 12)sma9 = ta.sma(close, 13)sma10 = ta.sma(close, 14)sma11 = ta.sma(close, 15)sma12 = ta.sma(close, 16)sma13 = ta.sma(close, 17)sma14 = ta.sma(close, 18)sma15 = ta.sma(close, 19)sma16 = ta.sma(close, 20)psar = ta.sar(0.02, 0.02, 0.2)[supertrend, direction] = supertrend(close, sensitivity, 11)barsL = 10barsR = 10pivotHigh = fixnan(ta.pivothigh(barsL, barsR)[1])pivotLow = fixnan(ta.pivotlow(barsL, barsR)[1])// Colorsgreen = #04994b, green2 = #15c02ared = #b4060d, red2 = #ff0002

p5 = plot(ocAvg, "", na, editable=false)p6 = plot(psar, "PSAR", usePsar ? (psar < ocAvg ? green : red) : na, 1,plot.style_circles, editable=false)fill(p5, p6, usePsar ? (psar < ocAvg ? color.new(green, 90) : color.new(red, 90)) :na, editable=false)y1 = low - (ta.atr(30) * 2)y2 = high + (ta.atr(30) * 2)bull = ta.crossover(close, supertrend) and close >= sma9bear = ta.crossunder(close, supertrend) and close <= sma9buy = bull ? label.new(bar_index, y1, "▲", xloc.bar_index, yloc.price, #04994b,label.style_label_up, color.white, size.normal) : nasell = bear ? label.new(bar_index, y2, "▼", xloc.bar_index, yloc.price, #b4060d,label.style_label_down, color.white, size.normal) : na

// Strong TP Points //

maj_qual = 13maj_len = 40min_qual = 5min_len = 5min = false

selll = 0.0buyy = 0.0 lele(qual, len) => bindex = 0.0 sindex = 0.0 bindex := nz(bindex[1], 0) sindex := nz(sindex[1], 0) ret = 0 if close > close[4] bindex += 1 bindex if close < close[4] sindex += 1 sindex if bindex > qual and close < open and high >= ta.highest(high, len) bindex := 0 ret := -1 ret if sindex > qual and close > open and low <= ta.lowest(low, len) sindex := 0 ret := 1 ret return_1 = ret return_1

major = lele(maj_qual, maj_len)minor = lele(min_qual, min_len)

if minor == -1 and min == true selll := 1 selllif major == -1 and maj == true selll := 2 selllif major == -1 and maj == true and minor == -1 and min == true selll := 3 selll

if minor == 1 and min == true buyy := 1 buyyif major == 1 and maj == true buyy := 2 buyyif major == 1 and maj == true and minor == 1 and min == true buyy := 3 buyy

plotshape(selll == 2, style=shape.xcross, location=location.abovebar,color=color.new(#354996, 0), textcolor=color.new(color.white, 0), offset=0)

plotshape(buyy == 2, style=shape.xcross, location=location.belowbar,color=color.new(#354996, 0), textcolor=color.new(color.white, 0), offset=0)

// Ha Market Bias //

tf(_res, _exp, gaps_on) => gaps_on == 0 ? request.security(syminfo.tickerid, _res, _exp) : gaps_on == true? request.security(syminfo.tickerid, _res, _exp, barmerge.gaps_on,barmerge.lookahead_off) : request.security(syminfo.tickerid, _res, _exp, barmerge.gaps_off, barmerge.lookahead_off)

ha_htf = ''ha_len = 100ha_len2 = 100

// Calculations {o = ta.ema(open, ha_len)c = ta.ema(close, ha_len)h = ta.ema(high, ha_len)l = ta.ema(low, ha_len)

haclose = tf(ha_htf, (o + h + l + c) / 4, 0)xhaopen = tf(ha_htf, (o + c) / 2, 0)haopen = na(xhaopen[1]) ? (o + c) / 2 : (xhaopen[1] + haclose[1]) / 2hahigh = math.max(h, math.max(haopen, haclose))halow = math.min(l, math.min(haopen, haclose))

o2 = tf(ha_htf, ta.ema(haopen, ha_len2), 0)c2 = tf(ha_htf, ta.ema(haclose, ha_len2), 0)h2 = tf(ha_htf, ta.ema(hahigh, ha_len2), 0)l2 = tf(ha_htf, ta.ema(halow, ha_len2), 0)

ha_avg = (h2 + l2) / 2// }

// Oscillator {osc_len = 7

osc_bias = 100 *(c2 - o2)osc_smooth = ta.ema(osc_bias, osc_len)

sigcolor = (osc_bias > 0) and (osc_bias >= osc_smooth) ? color.new(color.lime, 35) : (osc_bias > 0) and (osc_bias < osc_smooth) ? color.new(color.lime, 75) : (osc_bias < 0) and (osc_bias <= osc_smooth) ? color.new(color.red, 35) : (osc_bias < 0) and (osc_bias > osc_smooth) ? color.new(color.red, 75) : na// }

// Plots {p_h = plot(h2, "Bias High", color=color(na), display=display.none, editable=false)p_l = plot(l2, "Bias Low", color=color(na), display=display.none, editable=false)p_avg = plot(ha_avg, "Bias Avergae", color=color(na), display=display.none,editable=false)

fill(p_l, p_h, show_ha ? sigcolor : na)col = o2 > c2 ? color.red : color.lime// }

// Range Filter DW

//---------------------RangeFilter---------------------------------------------------------------------------------------------------------------------- //Conditional Sampling EMA FunctionCond_EMA(x, cond, n) => var val = array.new_float(0) var ema_val = array.new_float(1) if cond array.push(val, x) if array.size(val) > 1 array.remove(val, 0) if na(array.get(ema_val, 0)) array.fill(ema_val, array.get(val, 0)) array.set(ema_val, 0, (array.get(val, 0) - array.get(ema_val, 0)) * (2 / (n+ 1)) + array.get(ema_val, 0)) EMA = array.get(ema_val, 0) EMA

//Conditional Sampling SMA FunctionCond_SMA(x, cond, n) => var vals = array.new_float(0) if cond array.push(vals, x) if array.size(vals) > n array.remove(vals, 0) SMA = array.avg(vals) SMA

//Standard Deviation FunctionStdev(x, n) => math.sqrt(Cond_SMA(math.pow(x, 2), 1, n) - math.pow(Cond_SMA(x, 1, n), 2))

//Range Size Functionrng_size(x, scale, qty, n) => ATR = Cond_EMA(ta.tr(true), 1, n) AC = Cond_EMA(math.abs(x - x[1]), 1, n) SD = Stdev(x, n) rng_size = scale == 'Pips' ? qty * 0.0001 : scale == 'Points' ? qty *syminfo.pointvalue : scale == '% of Price' ? close * qty / 100 : scale == 'ATR' ?qty * ATR : scale == 'Average Change' ? qty * AC : scale == 'Standard Deviation' ?qty * SD : scale == 'Ticks' ? qty * syminfo.mintick : qty rng_size

//Two Type Range Filter Functionrng_filt(h, l, rng_, n, type, smooth, sn, av_rf, av_n) => rng_smooth = Cond_EMA(rng_, 1, sn) r = smooth ? rng_smooth : rng_ var rfilt = array.new_float(2, (h + l) / 2) array.set(rfilt, 1, array.get(rfilt, 0)) if type == 'Type 1' if h - r > array.get(rfilt, 1) array.set(rfilt, 0, h - r) if l + r < array.get(rfilt, 1) array.set(rfilt, 0, l + r) if type == 'Type 2' if h >= array.get(rfilt, 1) + r array.set(rfilt, 0, array.get(rfilt, 1) + math.floor(math.abs(h -array.get(rfilt, 1)) / r) * r) if l <= array.get(rfilt, 1) - r array.set(rfilt, 0, array.get(rfilt, 1) - math.floor(math.abs(l -array.get(rfilt, 1)) / r) * r) rng_filt1 = array.get(rfilt, 0) hi_band1 = rng_filt1 + r lo_band1 = rng_filt1 - r rng_filt2 = Cond_EMA(rng_filt1, rng_filt1 != rng_filt1[1], av_n) hi_band2 = Cond_EMA(hi_band1, rng_filt1 != rng_filt1[1], av_n) lo_band2 = Cond_EMA(lo_band1, rng_filt1 != rng_filt1[1], av_n) rng_filt = av_rf ? rng_filt2 : rng_filt1 hi_band = av_rf ? hi_band2 : hi_band1 lo_band = av_rf ? lo_band2 : lo_band1 [hi_band, lo_band, rng_filt]

//-----------------------------------------------------------------------------------------------------------------------------------------------------------------//Inputs//-----------------------------------------------------------------------------------------------------------------------------------------------------------------

//Filter Typef_type = 'Type 2'

//Movement Sourcemov_src = 'Close'

//Range Size Inputsrng_qty = 2.618rng_scale = 'Average Change'

//Range Periodrng_per = 14

//Range Smoothing Inputssmooth_range = truesmooth_per = 27

//Filter Value Averaging Inputsav_vals = falseav_samples = 2

//-----------------------------------------------------------------------------------------------------------------------------------------------------------------//Definitions//-----------------------------------------------------------------------------------------------------------------------------------------------------------------

//High And Low Valuesh_val = mov_src == 'Wicks' ? high : closel_val = mov_src == 'Wicks' ? low : close

//Range Filter Values[h_band, l_band, filt] = rng_filt(h_val, l_val, rng_size((h_val + l_val) / 2,rng_scale, rng_qty, rng_per), rng_per, f_type, smooth_range, smooth_per, av_vals,av_samples)

//Direction Conditionsvar fdir = 0.0fdir := filt > filt[1] ? 1 : filt < filt[1] ? -1 : fdirupward = fdir == 1 ? 1 : 0downward = fdir == -1 ? 1 : 0

//Colors filt_color = upward ? #36db7f : downward ? #be130f : #cccccc

//-----------------------------------------------------------------------------------------------------------------------------------------------------------------//Outputs//-----------------------------------------------------------------------------------------------------------------------------------------------------------------

//Filter Plotfilt_plot = plot(Show_rangefilter ? filt : na, color=filt_color, linewidth=3,title='Filter', transp=0)

//Bar Color

//External Trend Outputplot(fdir, editable=false, display=display.none, title='External Output - TrendSignal', transp=100)

// Superlchi + TBO

tenkan_len = 6tenkan_mult = 2

kijun_len = 5kijun_mult = 3.

spanB_len = 26spanB_mult = 4.

offset = 0//------------------------------------------------------------------------------avg(srcc,length,mult)=> atr = ta.atr(length)*mult up = hl2 + atr dn = hl2 - atr upper = 0.,lower = 0. upper := srcc[1] < upper[1] ? math.min(up,upper[1]) : up lower := srcc[1] > lower[1] ? math.max(dn,lower[1]) : dn

os = 0,max = 0.,min = 0. os := srcc > upper ? 1 : srcc < lower ? 0 : os[1] spt = os == 1 ? lower : upper max := ta.cross(srcc,spt) ? math.max(srcc,max[1]) : os == 1 ?math.max(srcc,max[1]) : spt min := ta.cross(srcc,spt) ? math.min(srcc,min[1]) : os == 0 ?math.min(srcc,min[1]) : spt math.avg(max,min)//------------------------------------------------------------------------------tenkan = avg(close,tenkan_len,tenkan_mult)kijun = avg(close,kijun_len,kijun_mult)

senkouA = math.avg(kijun,tenkan)senkouB = avg(close,spanB_len,spanB_mult)//------------------------------------------------------------------------------tenkan_css = #2157f3kijun_css = #ff5d00

cloud_a = color.new(color.teal,80) cloud_b = color.new(color.red,80)

chikou_css = #7b1fa2

plot(Show_SuperIchi ? tenkan : na,'Tenkan-Sen',tenkan_css)plot(Show_SuperIchi ? kijun : na,'Kijun-Sen',kijun_css)

plot(ta.crossover(tenkan,kijun) ? kijun :na,'Crossover',#2157f3,3,plot.style_circles)plot(ta.crossunder(tenkan,kijun) ? kijun :na,'Crossunder',#ff5d00,3,plot.style_circles)

A = plot(Show_SuperIchi ? senkouA : na,'Senkou Span A',na,offset=offset-1)B = plot(Show_SuperIchi ? senkouB : na,'Senkou Span B',na,offset=offset-1)fill(A,B,senkouA > senkouB ? cloud_a : cloud_b)

plot(close,'Chikou',chikou_css,offset=-offset+1,display=display.none)

//------------------------- TBO | https://www.thebettertraders.com -----------//// Get user inputbool enableCustomTBO = input(false, "Enable?", "Custom trend settings are notenabled by default. The default settings loaded are not shown publicly. You havethe option to enter your own custom settings as you get more familiar with theTBO.", group="CUSTOM TREND STRENGTH SETTINGS")var fastLen = input.int(1, "TBO Fast", 1, group="CUSTOM TREND STRENGTHSETTINGS")var mediumLen = input.int(2, "TBO Medium", 2, group="CUSTOM TREND STRENGTHSETTINGS")var medfastLen = input.int(3, "TBO Med Fast", 3, group="CUSTOM TRENDSTRENGTH SETTINGS")var slowLen = input.int(4, "TBO Slow", 4, group="CUSTOM TREND STRENGTHSETTINGS")bool enableRSI = input(false, "Enable?", "Enable this if you wish to combinean RSI requirement with the TBO Long or TBO Short signal. The default settingsshown here have no importance, they are just placeholders and are not significant.It is raccomended to have the RSI showing when this is enabled so you can see whatkind of settings will work.", group="TBO LONG/SHORT W/ RSI")var shortRsiBand = input.int(70, "Short RSI Band", 1, 100, group="TBOLONG/SHORT W/ RSI")var shortBandGL = input.string("Greater Than", "Greater/Less Than", ["GreaterThan", "Less Than"], group="TBO LONG/SHORT W/ RSI")var longRsiBand = input.int(30, "Long RSI Band", 1, 100, group="TBOLONG/SHORT W/ RSI")var longBandGL = input.string("Less Than", "Greater/Less Than", ["GreaterThan", "Less Than"], group="TBO LONG/SHORT W/ RSI")var rsiLen = input.int(14, "TBO Med Fast", 1, group="TBO LONG/SHORT W/RSI")bool enableTP = input(false, "Enable?", group="TAKE PROFIT SETTINGS")var longTPperc = input.int(9, "TP Long %", 1, group="TAKE PROFIT SETTINGS")var shortTPperc = input.int(9, "TP Short %", 1, group="TAKE PROFIT SETTINGS")bool static = input(false, "Static", "If enabled will plot a signal everytime volume gets greater than your defined value.", group="DHP VOLUME SCALPING")var volThreshold = input.int(20000, "Volume", 1, group="DHP VOLUME SCALPING")bool maMultiple = input(false, "MA Multiple", "If enabled will plot a signalevery time volume gets greater than his average multiplied by your defined value.",group="DHP VOLUME SCALPING")var average = input.int(20, "Average", 2, tooltip="Number of bars backused to calculate the volume's average.", group="DHP VOLUME SCALPING")var multipleX = input.int(3, "Multiple X", 1, tooltip="Number of times the volume's average will be multiplied.", group="DHP VOLUME SCALPING")// Functionsbb(src, len, mult) => float basis = ta.ema(src, len) float dev = mult * ta.stdev(src, len) [basis, basis + dev, basis - dev][_, upperBB, lowerBB] = bb(close, 25, 1)isLast(var1, var2) => ta.barssince(var1) < ta.barssince(var2)// Get componentsfloat fastTBO = ta.ema(close, enableCustomTBO ? fastLen : 20)float mediumTBO = ta.ema(close, enableCustomTBO ? mediumLen : 40)float medfastTBO = ta.sma(close, enableCustomTBO ? medfastLen : 50)float slowTBO = ta.sma(close, enableCustomTBO ? slowLen : 150)float rsi = ta.rsi(close, rsiLen)bool rsiShort = enableRSI and shortBandGL == "Greater Than" ? (rsi >shortRsiBand) : (rsi < shortRsiBand)bool rsiLong = enableRSI and longBandGL == "Less Than" ? (rsi <longRsiBand) : (rsi > longRsiBand)float vol = volumefloat volMA = ta.sma(vol, average) * multipleXbool openLong = ta.crossover(fastTBO, mediumTBO) and rsiLong, lastLong =ta.barssince(openLong), long = ta.crossover(fastTBO, mediumTBO)bool openShort = ta.crossunder(fastTBO, mediumTBO) and rsiShort, lastShort =ta.barssince(openShort), short = ta.crossunder(fastTBO, mediumTBO)

// Colorsgreenn = #2FD282pink = #E34DED// Plots

plotshape(Show_TBO ? openLong : na, "▲ Open Long", shape.triangleup,location.belowbar, greenn, size=size.tiny)plotshape(Show_TBO ? openShort : na, "▼ Open Short", shape.triangledown,location.abovebar, pink, size=size.tiny)

// Smart TrailtrailType = input.string('modified', 'Trailtype', options=['modified','unmodified'])ATRPeriod = input(13, 'ATR Period')ATRFactor = input(4, 'ATR Factor')smoothing = input(8, 'Smoothing')

norm_o = request.security(ticker.new(syminfo.prefix, syminfo.ticker),timeframe.period, open)norm_h = request.security(ticker.new(syminfo.prefix, syminfo.ticker),timeframe.period, high)norm_l = request.security(ticker.new(syminfo.prefix, syminfo.ticker),timeframe.period, low)norm_c = request.security(ticker.new(syminfo.prefix, syminfo.ticker),timeframe.period, close)//}

//////// FUNCTIONS ////////////////{// Wilders ma //Wild_ma(_src, _malength) => _wild = 0.0 _wild := nz(_wild[1]) + (_src - nz(_wild[1])) / _malength _wild /////////// TRUE RANGE CALCULATIONS /////////////////HiLo = math.min(norm_h - norm_l, 1.5 * nz(ta.sma(norm_h - norm_l, ATRPeriod)))

HRef = norm_l <= norm_h[1] ? norm_h - norm_c[1] : norm_h - norm_c[1] - 0.5 *(norm_l - norm_h[1])

LRef = norm_h >= norm_l[1] ? norm_c[1] - norm_l : norm_c[1] - norm_l - 0.5 *(norm_l[1] - norm_h)

trueRange = trailType == 'modified' ? math.max(HiLo, HRef, LRef) : math.max(norm_h- norm_l, math.abs(norm_h - norm_c[1]), math.abs(norm_l - norm_c[1]))//}

/////////// TRADE LOGIC //////////////////////////{loss = ATRFactor * Wild_ma(trueRange, ATRPeriod)

Up = norm_c - lossDn = norm_c + loss

TrendUp = UpTrendDown = DnTrend = 1

TrendUp := norm_c[1] > TrendUp[1] ? math.max(Up, TrendUp[1]) : UpTrendDown := norm_c[1] < TrendDown[1] ? math.min(Dn, TrendDown[1]) : Dn

Trend := norm_c > TrendDown[1] ? 1 : norm_c < TrendUp[1] ? -1 : nz(Trend[1], 1)trail = Trend == 1 ? TrendUp : TrendDown

ex = 0.0ex := ta.crossover(Trend, 0) ? norm_h : ta.crossunder(Trend, 0) ? norm_l : Trend ==1 ? math.max(ex[1], norm_h) : Trend == -1 ? math.min(ex[1], norm_l) : ex[1]//}

// //////// PLOT TP and SL /////////////

////// FIBONACCI LEVELS /////////////{state = Trend == 1 ? 'long' : 'short'

fib1Level = 61.8fib2Level = 78.6fib3Level = 88.6

f1 = ex + (trail - ex) * fib1Level / 100f2 = ex + (trail - ex) * fib2Level / 100f3 = ex + (trail - ex) * fib3Level / 100l100 = trail + 0

fill(plot(ShowSmartTrail ? (ta.sma(trail, smoothing)) : na, 'Trailingstop',style=plot.style_line, color=Trend == 1 ? color.new(#2157f9, 0) : Trend == -1 ?color.new(#ff1100, 0) : na), plot( ShowSmartTrail ? (ta.sma(f2, smoothing)) : na, 'Fib 2',style=plot.style_line, display=display.none), color=state == 'long' ? color.new(#2157f9, 80) : state == 'short' ?color.new(#ff1100, 80) : na) //}

// Reversal Signals

ReversalInputs = input.int(14, minval=1, title="Reversals Sensitivity",group="Reversal Settings")overbought = input(75, 'Reversal Down Level', group='Reversal Settings')oversold = input(25, 'Reversal Up Level', group='Reversal Settings')

upwardd = ta.rma(math.max(ta.change(close), 0), ReversalInputs)dnwardd = ta.rma(-math.min(ta.change(close), 0), ReversalInputs)source = dnwardd == 0 ? 100 : upwardd == 0 ? 0 : 100 - (100 / (1 + upwardd /dnwardd))

revdn = ta.crossunder(source, overbought) and enableReversalrevup = ta.crossover(source, oversold) and enableReversal

plotshape(revup, 'Reversal Up Signal', shape.labelup, location.belowbar,color.new(#2157f9, 65), text='Reversal Up Chance', size=size.small,textcolor=color.white)plotshape(revdn, 'Reversal Down Signal', shape.labeldown, location.abovebar,color.new(#ff1100, 65), text='Reversal Down Chance', size=size.small,textcolor=color.white)

// EzAlgo SR

// Get user inputcolorSup = #04994bcolorRes = #b4060dstrengthSR = input.int(4, "Support&Resistance Strength", 1, group="SR")lineStyle = input.string("Solid", "Line Style", ["Solid", "Dotted", "Dashed"],group="SR")lineWidth = 2useZones = input(true, "SR Zones", group="SR")useHLZones = useZoneszoneWidth = 2expandSR = true// FunctionspercWidth(len, perc) => (ta.highest(len) - ta.lowest(len)) * perc / 100// Get componentsrb = 10prd = 284ChannelW = 10label_loc = 55style = lineStyle == "Solid" ? line.style_solid : lineStyle == "Dotted" ?line.style_dotted : line.style_dashedph = ta.pivothigh(rb, rb)pl = ta.pivotlow (rb, rb)sr_levels = array.new_float(21, na)prdhighest = ta.highest(prd)prdlowest = ta.lowest(prd)cwidth = percWidth(prd, ChannelW)zonePerc = percWidth(300, zoneWidth)aas = array.new_bool(41, true)u1 = 0.0, u1 := nz(u1[1])d1 = 0.0, d1 := nz(d1[1])highestph = 0.0, highestph := highestph[1]lowestpl = 0.0, lowestpl := lowestpl[1]var sr_levs = array.new_float(21, na) var sr_lines = array.new_line(21, na)var sr_linesH = array.new_line(21, na)var sr_linesL = array.new_line(21, na)var sr_linesF = array.new_linefill(21, na)var sr_labels = array.new_label(21, na)if ph or pl for x = 0 to array.size(sr_levels) - 1 array.set(sr_levels, x, na) highestph := prdlowest lowestpl := prdhighest countpp = 0 for x = 0 to prd if na(close[x]) break if not na(ph[x]) or not na(pl[x]) highestph := math.max(highestph, nz(ph[x], prdlowest), nz(pl[x],prdlowest)) lowestpl := math.min(lowestpl, nz(ph[x], prdhighest), nz(pl[x],prdhighest)) countpp += 1 if countpp > 40 break if array.get(aas, countpp) upl = (ph[x] ? high[x + rb] : low[x + rb]) + cwidth dnl = (ph[x] ? high[x + rb] : low[x + rb]) - cwidth u1 := countpp == 1 ? upl : u1 d1 := countpp == 1 ? dnl : d1 tmp = array.new_bool(41, true) cnt = 0 tpoint = 0 for xx = 0 to prd if na(close[xx]) break if not na(ph[xx]) or not na(pl[xx]) chg = false cnt += 1 if cnt > 40 break if array.get(aas, cnt) if not na(ph[xx]) if high[xx + rb] <= upl and high[xx + rb] >= dnl tpoint += 1 chg := true if not na(pl[xx]) if low[xx + rb] <= upl and low[xx + rb] >= dnl tpoint += 1 chg := true if chg and cnt < 41 array.set(tmp, cnt, false) if tpoint >= strengthSR for g = 0 to 40 by 1 if not array.get(tmp, g) array.set(aas, g, false) if ph[x] and countpp < 21 array.set(sr_levels, countpp, high[x + rb]) if pl[x] and countpp < 21 array.set(sr_levels, countpp, low[x + rb])// Plotvar line highest_ = na, line.delete(highest_) var line lowest_ = na, line.delete(lowest_)var line highest_fill1 = na, line.delete(highest_fill1)var line highest_fill2 = na, line.delete(highest_fill2)var line lowest_fill1 = na, line.delete(lowest_fill1)var line lowest_fill2 = na, line.delete(lowest_fill2)hi_col = close >= highestph ? colorSup : colorReslo_col = close >= lowestpl ? colorSup : colorResif enableSR highest_ := line.new(bar_index - 311, highestph, bar_index, highestph,xloc.bar_index, expandSR ? extend.both : extend.right, hi_col, style, lineWidth) lowest_ := line.new(bar_index - 311, lowestpl , bar_index, lowestpl ,xloc.bar_index, expandSR ? extend.both : extend.right, lo_col, style, lineWidth) if useHLZones highest_fill1 := line.new(bar_index - 311, highestph + zonePerc, bar_index,highestph + zonePerc, xloc.bar_index, expandSR ? extend.both : extend.right, na) highest_fill2 := line.new(bar_index - 311, highestph - zonePerc, bar_index,highestph - zonePerc, xloc.bar_index, expandSR ? extend.both : extend.right, na) lowest_fill1 := line.new(bar_index - 311, lowestpl + zonePerc , bar_index,lowestpl + zonePerc , xloc.bar_index, expandSR ? extend.both : extend.right, na) lowest_fill2 := line.new(bar_index - 311, lowestpl - zonePerc , bar_index,lowestpl - zonePerc , xloc.bar_index, expandSR ? extend.both : extend.right, na) linefill.new(highest_fill1, highest_fill2, color.new(hi_col, 80)) linefill.new(lowest_fill1 , lowest_fill2 , color.new(lo_col, 80))if ph or pl for x = 0 to array.size(sr_lines) - 1 array.set(sr_levs, x, array.get(sr_levels, x))for x = 0 to array.size(sr_lines) - 1 line.delete(array.get(sr_lines, x)) line.delete(array.get(sr_linesH, x)) line.delete(array.get(sr_linesL, x)) linefill.delete(array.get(sr_linesF, x)) if array.get(sr_levs, x) and enableSR line_col = close >= array.get(sr_levs, x) ? colorSup : colorRes array.set(sr_lines, x, line.new(bar_index - 355, array.get(sr_levs, x),bar_index, array.get(sr_levs, x), xloc.bar_index, expandSR ? extend.both :extend.right, line_col, style, lineWidth)) if useZones array.set(sr_linesH, x, line.new(bar_index - 355, array.get(sr_levs, x)+ zonePerc, bar_index, array.get(sr_levs, x) + zonePerc, xloc.bar_index, expandSR ?extend.both : extend.right, na)) array.set(sr_linesL, x, line.new(bar_index - 355, array.get(sr_levs, x)- zonePerc, bar_index, array.get(sr_levs, x) - zonePerc, xloc.bar_index, expandSR ?extend.both : extend.right, na)) array.set(sr_linesF, x, linefill.new(array.get(sr_linesH, x),array.get(sr_linesL, x), color.new(line_col, 80)))

// Lux Algo Reversal Band

//funckama(ssrc, llen) => kama = 0.0 sum_1 = math.sum(math.abs(ssrc - ssrc[1]), llen) sum_2 = math.sum(math.abs(ssrc - ssrc[1]), llen) kama := nz(kama[1]) + math.pow((sum_1 != 0 ? math.abs(ssrc - ssrc[llen]) /sum_2 : 0) * (0.288 - 0.0666) + 0.0666, 2) * (ssrc - nz(kama[1])) kama

//inputsllength = input(50, title='Band Length') bd1 = input(9, title='Frontrun Band Deviation')bd2 = input(11, title='Initial Band Deviation')bd3 = input(14, title='Final Band Deviation')

//logicrg = kama(ta.tr, llength)basis = kama(close, llength)upper1 = basis + rg * bd1upper2 = basis + rg * bd2upper3 = basis + rg * bd3lower1 = basis - rg * bd1lower2 = basis - rg * bd2lower3 = basis - rg * bd3

//plotingpp1 = plot(show_rev ? upper1 : na, transp=100)pp2 = plot(show_rev ? upper2 : na, transp=100)pp3 = plot(show_rev ? upper3 : na, transp=100)pp4 = plot(show_rev ? lower1 : na, transp=100)pp5 = plot(show_rev ? lower2 : na, transp=100)pp6 = plot(show_rev ? lower3 : na, transp=100)fill(pp1, pp2, color=color.new(#57202c, 70))fill(pp2, pp3, color=color.new(#57202c, 50))fill(pp4, pp5, color=color.new(#103c3c, 70))fill(pp5, pp6, color=color.new(#103c3c, 50))

// Candle Coloring

// InputfastLength = input(title="Fast Length", defval=12)slowLength = input(title="Slow Length", defval=26)srrrc = input(title="Source", defval=close)signalLength = input.int(title="Signal Smoothing", minval = 1, maxval = 50, defval= 9)

// Data reference[macd, signal, hist] = ta.macd(srrrc, fastLength, slowLength, signalLength)

// 4 level of greengreenHigh = #05df09greenMidHigh = #05df09greenMidLow = #388E3CgreenLow = #5f3a97

// YellowyellowLow = #5f3a97

// 4 level of redredHigh = #ea0402redMidHigh = #ea0402redMidLow = #cc0402redLow = #5f3a97

// Default colorcandleBody = yellowLow

// Ranging trendif hist > 0 if hist > hist[1] and hist[1] > 0 candleBody := greenLow

if hist < 0 if hist < hist[1] and hist[1] < 0 candleBody := redLow

// Bullish trendif macd > 0 and hist > 0 candleBody := greenMidLow

if hist > hist[1] and macd[1] > 0 and hist[1] > 0 candleBody := greenMidHigh

if hist > hist[2] and macd[2] > 0 and hist[2] > 0 candleBody := greenHigh

// Bearish trendif macd < 0 and hist < 0 candleBody := redMidLow

if hist < hist[1] and macd[1] < 0 and hist[1] < 0 candleBody := redMidHigh

if hist < hist[2] and macd[2] < 0 and hist[2] < 0 candleBody := redHigh

barcolor(candleBody) // Include suggestion by Shaheen204

© 2021 Scribd.VDownloaders.com

Scribd.VDownloaders.com não está afiliado a quaisquer websites (tais como Scribd.com e Slideshare.net). Não armazenamos nenhum ficheiro nos nossos servidores.

About Us Terms of Services Privacy Policy Disclaimer
