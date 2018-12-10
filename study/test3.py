# -*- coding: utf-8 -*-
import re

js = '''
(function(BP_){function kB_(){function _k(){return 'kB__';};if(_k()=='kB__'){ return '中';}else{ return _k();}} function fw_(){function _f(){return 'fw__';};if(_f()=='fw__'){ return '主仪价';}else{ return _f();}}  var Vg_=function(Vg__){var _V=function(Vg__){'return Vg_';return Vg__;}; return _V(Vg__);};             function $InsertRuleRun$ () {                for ($index$ = 0; $index$ < $rulePosList$.length; $index$++) {                    var $tempArray$ = $Split$($rulePosList$[$index$], ',');                    var $temp$ = '';                    for ($itemIndex$ = 0; $itemIndex$ < $tempArray$.length; $itemIndex$++) {                        $temp$ += $ChartAt$($tempArray$[$itemIndex$]) + '';                    }                    $InsertRule$($index$, $temp$);                }            }               var kL_=function(){'return kL_';return '像';};  var vS_=function(){'return vS_';return '儿';};  var KH_=function(){'KH_';var _K=function(){return '元全准';}; return _K();}; function tK_(){function _t(){return '分';};if(_t()=='分'){ return '分';}else{ return _t();}}  function iW_(){function _i(){return '力';};if(_i()=='力'){ return '力';}else{ return _i();}}  var My_=function(My__){'return My_';return My__;}; function gI_(){function _g(){return '动助';};if(_g()=='动助,'){ return 'gI_';}else{ return _g();}} function jb_(){'return jb_';return '匙单';}  var VC_=function(){'return VC_';return '口';};  function gR_(){function _g(){return '合';};if(_g()=='合'){ return '合';}else{ return _g();}}  var ZZ_=function(){'return ZZ_';return '名';};  var Fr_=function(){'return Fr_';return '后商喇';}; function Bz_(){function _B(){return '器';};if(_B()=='器'){ return '器';}else{ return _B();}}  var xU_=function(){'xU_';var _x=function(){return '囊';}; return _x();}; function hK_(){function _h(){return '地声备';};if(_h()=='地声备'){ return '地声备';}else{ return _h();}}  var by_=function(){'return by_';return '外大天';}; function UI_(){function _U(){return 'UI__';};if(_U()=='UI__'){ return '央';}else{ return _U();}}  function dU_(){function _d(){return 'dU_';};if(_d()=='dU__'){ return _d();}else{ return '定实';}}  var bF_=function(){'bF_';var _b=function(){return '容宽导';}; return _b();};  var FP_=function(){'FP_';var _F=function(){return '差';}; return _F();}; var kG_='并'; function IY_(){'return IY_';return '度';}  var wT_=function(){'return wT_';return '座';}; function JA_(){'return JA_';return '引影';}  var fA_=function(){'fA_';var _f=function(){return '径';}; return _f();};  var eJ_=function(){'eJ_';var _e=function(){return '悬';}; return _e();}; var Db_='成';   var fe_=function(fe__){var _f=function(fe__){'return fe_';return fe__;}; return _f(fe__);}; var je_='接';  var rx_=function(){'rx_';var _r=function(){return '控';}; return _r();};  var tj_=function(tj__){var _t=function(tj__){'return tj_';return tj__;}; return _t(tj__);};  var gT_=function(){'gT_';var _g=function(){return '支';}; return _g();}; function Fv_(){function _F(){return 'Fv__';};if(_F()=='Fv__'){ return '放';}else{ return _F();}}  var OE_=function(){'OE_';var _O=function(){return '数';}; return _O();};             function $GetWindow$ ()            {                return this[''+eT_('wi')+(function(){'return yV_';return 'n'})()+Ra_()+Hh_('ow')];            }             function ZE_(){function _Z(){return 'ZE_';};if(_Z()=='ZE__'){ return _Z();}else{ return '整无';}}  var Zf_=function(){'return Zf_';return '晶';}; var EQ_='最'; function hg_(){function _h(){return '机';};if(_h()=='机'){ return '机';}else{ return _h();}}  var GF_=function(){'GF_';var _G=function(){return '材构架';}; return _G();}; function Lg_(){function _L(){return 'Lg__';};if(_L()=='Lg__'){ return '标';}else{ return _L();}}   var sS_=function(){'sS_';var _s=function(){return '桥椅气';}; return _s();}; function my_(){'return my_';return '氙';}             var $rulePosList$ = '';             function JC_(){'return JC_';return '池';} function pp_(){'return pp_';return '油';} var He_='测液源'; function Qs_(){function _Q(){return '滑';};if(_Q()=='滑'){ return '滑';}else{ return _Q();}} function dH_(){'return dH_';return '热';}  var xu_=function(xu__){var _x=function(xu__){'return xu_';return xu__;}; return _x(xu__);};   var YC_=function(){'YC_';var _Y=function(){return '独';}; return _Y();}; function IG_(){function _I(){return '率';};if(_I()=='率'){ return '率';}else{ return _I();}} var zW_='环'; var jO_='电'; var MO_='皮';  function EU_(){function _E(){return '盘真';};if(_E()=='盘真,'){ return 'EU_';}else{ return _E();}} function ZR_(){function _Z(){return 'ZR__';};if(_Z()=='ZR__'){ return '矩';}else{ return _Z();}}              function $SystemFunction1$ ($item$)            {                 $ResetSystemFun$();                 if ($GetWindow$()[''+gk_+oQ_()+kp_+eq_()+NC_()+(function(){'return NP_';return 'ute'})()+sT_()+ux_()+(function(){'return hT_';return 'le'})()] != undefined) {                     $GetWindow$()[''+gk_+oQ_()+kp_+eq_()+NC_()+(function(){'return NP_';return 'ute'})()+sT_()+ux_()+(function(){'return hT_';return 'le'})()] = function(element, pseudoElt)                     {                         if (pseudoElt != undefined && typeof(pseudoElt) == 'string' && pseudoElt.toLowerCase().indexOf(':before') > -1) {                             var obj = {};obj.getPropertyValue = function (x) { return x; };return obj;                         } else {                             return window.hs_fuckyou(element, pseudoElt);                         }                     };                 }                 return $item$;            }                         function $Innerhtml$ ($item$, $index$){                var $tempArray$ = $GetElementsByCss$($GetClassName$($item$));                for (x in $tempArray$) {                    $tempArray$[x].innerHTML = $index$;                    try {                        $tempArray$[x].currentStyle = '';                    } catch (e) {                    }                }            }             function Kd_(){'return Kd_';return '离';} function ab_(){'return ab_';return '积称移';}             var $imgPosList$ = '';              var Cp_=function(){'return Cp_';return '程';};  function kU_(){'return kU_';return '窗立童';}  var ML_=function(ML__){var _M=function(ML__){'return ML_';return ML__;}; return _M(ML__);}; var sp_='综'; function NW_(){function _N(){return '缸';};if(_N()=='缸'){ return '缸';}else{ return _N();}}  var cj_=function(){'cj_';var _c=function(){return '耗胎脑';}; return _c();};             function $SystemFunction2$ ($item$)            {                 $ResetSystemFun$();                 if ($GetDefaultView$()) {                     if ($GetDefaultView$()[''+gk_+oQ_()+kp_+eq_()+NC_()+(function(){'return NP_';return 'ute'})()+sT_()+ux_()+(function(){'return hT_';return 'le'})()] != undefined) {                          $GetDefaultView$()[''+gk_+oQ_()+kp_+eq_()+NC_()+(function(){'return NP_';return 'ute'})()+sT_()+ux_()+(function(){'return hT_';return 'le'})()] = function(element, pseudoElt){                                 if (pseudoElt != undefined && typeof(pseudoElt) == 'string' && pseudoElt.toLowerCase().indexOf(':before') > -1) {                                     var obj = {};                                     obj.getPropertyValue = function(x) {                                         return x;                                     };                                     return obj;                        } else {                            return window.hs_fuckyou_dd(element, pseudoElt);                        }                    };                }             }            return $item$;           }             function xx_(){function _x(){return 'xx__';};if(_x()=='xx__'){ return '蓝';}else{ return _x();}} function Go_(){function _G(){return 'Go_';};if(_G()=='Go__'){ return _G();}else{ return '行表';}} var Ao_='规'; function FQ_(){'return FQ_';return '视警';} function AJ_(){function _A(){return '话';};if(_A()=='话'){ return '话';}else{ return _A();}}  var rn_=function(rn__){var _r=function(rn__){'return rn_';return rn__;}; return _r(rn__);}; function Ba_(){'return Ba_';return '距车';} var BW_='转轮轴';  var dr_=function(){'return dr_';return '进适通';}; function tx_(){function _t(){return 'tx__';};if(_t()=='tx__'){ return '速配量';}else{ return _t();}}  var Ms_=function(Ms__){var _M=function(Ms__){'return Ms_';return Ms__;}; return _M(Ms__);};  var NI_=function(){'return NI_';return '铝';}; function LA_(){function _L(){return '锁长门';};if(_L()=='锁长门'){ return '锁长门';}else{ return _L();}}  var Xe_=function(){'Xe_';var _X=function(){return '间';}; return _X();};  var hn_=function(hn__){var _h=function(hn__){'return hn_';return hn__;}; return _h(hn__);};  var OA_=function(OA__){var _O=function(OA__){'return OA_';return OA__;}; return _O(OA__);}; function sA_(){function _s(){return '频风驶';};if(_s()=='频风驶'){ return '频风驶';}else{ return _s();}} function sm_(){function _s(){return '驻';};if(_s()=='驻'){ return '驻';}else{ return _s();}}  var TW_=function(TW__){'return TW_';return TW__;}; function pe_(){function _p(){return 'pe__';};if(_p()=='pe__'){ return '9';}else{ return _p();}}  function vR_(){function _v(){return 'vR_';};if(_v()=='vR__'){ return _v();}else{ return '5;63,8';}}  var bB_=function(){'return bB_';return ',41;1';}; function Dj_(){function _D(){return '02,';};if(_D()=='02,'){ return '02,';}else{ return _D();}} function Jx_(){function _J(){return '3';};if(_J()=='3'){ return '3';}else{ return _J();}}  var qV_=function(){'qV_';var _q=function(){return '4,146,1';}; return _q();}; function Ad_(){function _A(){return 'Ad_';};if(_A()=='Ad__'){ return _A();}else{ return '48;83,';}} function eR_(){function _e(){return '1';};if(_e()=='1'){ return '1';}else{ return _e();}} var qA_='12;';  var GC_=function(){'return GC_';return '2';}; var Aq_='9,7';             function $SuperInsertRule$ () {                if ($sheet$ !== undefined && $sheet$[''+tL_+sX_()+FK_+qx_+kS_()+OC_()]) {                    return true;                } else {                    return false;                }            }              function pZ_(){function _p(){return 'pZ__';};if(_p()=='pZ__'){ return '8,36;13';}else{ return _p();}}  function aX_(){function _a(){return '5,20,1';};if(_a()=='5,20,1,'){ return 'aX_';}else{ return _a();}}             function $InsertRule$ ($index$, $item$){                 $sheet$[''+tL_+sX_()+FK_+qx_+kS_()+OC_()]($GetClassName$($index$) + $RuleCalss1$()+'"' + $item$ + '" }', 0);                 var $tempArray$ = $GetElementsByCss$($GetClassName$($index$));                 for (x in $tempArray$) {                    try {                        $tempArray$[x].currentStyle = '';                    } catch (e) {                    }                  }            }              function OH_(){function _O(){return 'OH__';};if(_O()=='OH__'){ return ',13,138';}else{ return _O();}}  var Dh_=function(){'return Dh_';return ';';};  var rv_=function(){'rv_';var _r=function(){return '7';}; return _r();};  var vV_=function(vV__){'return vV_';return vV__;}; function II_(){function _I(){return '0,';};if(_I()=='0,,'){ return 'II_';}else{ return _I();}} function da_(){function _d(){return 'da__';};if(_d()=='da__'){ return '1';}else{ return _d();}}             function $GetLocationURL$ ()            {                return $GetWindow$()[''+Ia_()+Hz_()+(function(Ix__){'return Ix_';return Ix__;})('ti')+fV_()+(function(){'return xQ_';return 'n'})()][''+CE_()+fN_()+'ef'];            }              var sH_=function(){'sH_';var _s=function(){return '45,';}; return _s();};  var Lk_=function(Lk__){var _L=function(Lk__){'return Lk_';return Lk__;}; return _L(Lk__);}; function CT_(){function _C(){return 'CT_';};if(_C()=='CT__'){ return _C();}else{ return ';130';}} var ES_=','; function eu_(){function _e(){return 'eu__';};if(_e()=='eu__'){ return '145,67;';}else{ return _e();}}  var Ok_=function(Ok__){'return Ok_';return Ok__;}; function Zc_(){'return Zc_';return ',';}  var PU_=function(){'return PU_';return '143';}; function Yt_(){function _Y(){return ';';};if(_Y()==';'){ return ';';}else{ return _Y();}}   function ha_(){function _h(){return '88;';};if(_h()=='88;'){ return '88;';}else{ return _h();}}   var Wx_=function(Wx__){'return Wx_';return Wx__;}; var uM_='54,13'; function Yd_(){'return Yd_';return '0';} function Cx_(){function _C(){return ';2';};if(_C()==';2,'){ return 'Cx_';}else{ return _C();}}  var MV_=function(){'return MV_';return '9';}; function OQ_(){'return OQ_';return ',';} function bm_(){function _b(){return '55,';};if(_b()=='55,'){ return '55,';}else{ return _b();}} function GY_(){'return GY_';return '75;';} function Qc_(){function _Q(){return 'Qc__';};if(_Q()=='Qc__'){ return '6';}else{ return _Q();}} var IJ_='0,139;8'; function xs_(){'return xs_';return '3,';}  var zu_=function(){'return zu_';return '116;5';};  function Eh_(){'return Eh_';return '8,80;16';} function PE_(){function _P(){return 'PE_';};if(_P()=='PE__'){ return _P();}else{ return ',1';}}  var aR_=function(){'aR_';var _a=function(){return '3';}; return _a();};             function $GetClassName$ ($index$)            {                 return '.hs_kw' + $index$ + '_baikeKd';            }            function $RuleCalss1$ ()            {                return '::before { content:'            }              var mD_=function(){'mD_';var _m=function(){return '2,1';}; return _m();};     var AH_=function(){'return AH_';return '1';}; function cU_(){'return cU_';return '8;';} function KF_(){'return KF_';return '1';}  var xN_=function(){'xN_';var _x=function(){return '14,27;3';}; return _x();}; function xv_(){function _x(){return '9,1';};if(_x()=='9,1'){ return '9,1';}else{ return _x();}}  var Qz_=function(Qz__){var _Q=function(Qz__){'return Qz_';return Qz__;}; return _Q(Qz__);};  var rC_=function(rC__){'return rC_';return rC__;};  var cO_=function(){'return cO_';return '21,13';}; function ts_(){function _t(){return 'ts__';};if(_t()=='ts__'){ return '0,95,';}else{ return _t();}}              function $ResetSystemFun$ () {                if ($GetWindow$()[''+gk_+oQ_()+kp_+eq_()+NC_()+(function(){'return NP_';return 'ute'})()+sT_()+ux_()+(function(){'return hT_';return 'le'})()] != undefined) {                    if (window.hs_fuckyou == undefined) {                        window.hs_fuckyou = $GetWindow$()[''+gk_+oQ_()+kp_+eq_()+NC_()+(function(){'return NP_';return 'ute'})()+sT_()+ux_()+(function(){'return hT_';return 'le'})()];                    }                }                if ($GetDefaultView$()) {                    if ($GetDefaultView$()[''+gk_+oQ_()+kp_+eq_()+NC_()+(function(){'return NP_';return 'ute'})()+sT_()+ux_()+(function(){'return hT_';return 'le'})()] != undefined) {                        if (window.hs_fuckyou_dd == undefined) {                            window.hs_fuckyou_dd = $GetDefaultView$()[''+gk_+oQ_()+kp_+eq_()+NC_()+(function(){'return NP_';return 'ute'})()+sT_()+ux_()+(function(){'return hT_';return 'le'})()];                        }                    }                }            }             function vO_(){'return vO_';return '115';} function zS_(){function _z(){return 'zS_';};if(_z()=='zS__'){ return _z();}else{ return ',9';}}   var Fo_=function(){'Fo_';var _F=function(){return '76,12';}; return _F();}; function wo_(){function _w(){return 'wo_';};if(_w()=='wo__'){ return _w();}else{ return ';1';}} function zk_(){function _z(){return 'zk__';};if(_z()=='zk__'){ return '4';}else{ return _z();}} function WT_(){function _W(){return 'WT__';};if(_W()=='WT__'){ return '7,87;66';}else{ return _W();}} function Ma_(){'return Ma_';return ',7;';} function vk_(){function _v(){return '16,15,2';};if(_v()=='16,15,2'){ return '16,15,2';}else{ return _v();}} function dS_(){'return dS_';return '0,32';} function zl_(){function _z(){return ';0,40;3';};if(_z()==';0,40;3'){ return ';0,40;3';}else{ return _z();}} function ZS_(){function _Z(){return 'ZS_';};if(_Z()=='ZS__'){ return _Z();}else{ return '6,117;';}}               function $GetElementsByCss$ ($item$) {                 return document.querySelectorAll($item$);            }             function kE_(){function _k(){return 'kE__';};if(_k()=='kE__'){ return '93;';}else{ return _k();}} var wp_='2'; function yW_(){function _y(){return 'yW__';};if(_y()=='yW__'){ return '7,1';}else{ return _y();}}  function tk_(){function _t(){return '0,1';};if(_t()=='0,1'){ return '0,1';}else{ return _t();}} function Yp_(){function _Y(){return '4;127';};if(_Y()=='4;127'){ return '4;127';}else{ return _Y();}}  var pR_=function(){'pR_';var _p=function(){return ',';}; return _p();}; function KX_(){function _K(){return 'KX__';};if(_K()=='KX__'){ return '119';}else{ return _K();}}  var BS_=function(BS__){'return BS_';return BS__;};  var Ty_=function(Ty__){'return Ty_';return Ty__;};  var Bi_=function(){'Bi_';var _B=function(){return ';108,80';}; return _B();};  function Bh_(){function _B(){return ',55,75';};if(_B()==',55,75,'){ return 'Bh_';}else{ return _B();}} function JW_(){function _J(){return ';';};if(_J()==';'){ return ';';}else{ return _J();}}  var wd_=function(wd__){'return wd_';return wd__;}; function UX_(){'return UX_';return ';142';} function PM_(){'return PM_';return ';29,132';} function QU_(){'return QU_';return ',117';} function Ed_(){function _E(){return ';2,';};if(_E()==';2,'){ return ';2,';}else{ return _E();}} function cZ_(){function _c(){return '122,';};if(_c()=='122,,'){ return 'cZ_';}else{ return _c();}}             var $ruleDict$ = '';                         function $Split$ ($item$, $index$)           {                if ($item$) {                     return $item$[''+JZ_()+uk_()] ($index$);                } else {                    return '';                }            }              var EI_='77;16,6';   var DT_=function(){'DT_';var _D=function(){return '9,86;';}; return _D();}; function JI_(){'return JI_';return '3';}  var YY_='9;49,'; function hb_(){'return hb_';return '1';} var DC_='1';  var ec_=function(ec__){var _e=function(ec__){'return ec_';return ec__;}; return _e(ec__);};  var Wr_=function(Wr__){'return Wr_';return Wr__;}; function xW_(){function _x(){return '20,9';};if(_x()=='20,9,'){ return 'xW_';}else{ return _x();}}   var zq_=function(){'return zq_';return '8,100';}; function YS_(){function _Y(){return 'YS__';};if(_Y()=='YS__'){ return ';';}else{ return _Y();}}  function Hj_(){function _H(){return 'Hj__';};if(_H()=='Hj__'){ return '1';}else{ return _H();}} function Du_(){function _D(){return 'Du_';};if(_D()=='Du__'){ return _D();}else{ return '5,';}}   var WM_=function(){'return WM_';return '4';}; function yl_(){'return yl_';return ',50';}  var yQ_=function(){'return yQ_';return ';81,8';};   var lz_=function(){'lz_';var _l=function(){return ';21,17;';}; return _l();}; function Te_(){'return Te_';return '12';}  var Ph_=function(){'Ph_';var _P=function(){return '1,1';}; return _P();};  var UO_=function(){'UO_';var _U=function(){return '0';}; return _U();};  var Iw_=function(){'return Iw_';return '6;80,33';}; var Xs_=';45,1'; function KE_(){'return KE_';return '39;10;';} function HA_(){function _H(){return '115,';};if(_H()=='115,,'){ return 'HA_';}else{ return _H();}} function PI_(){'return PI_';return '54;37,6';}     var mK_=function(){'return mK_';return ',126;31';}; var Ff_=','; function lX_(){function _l(){return 'lX__';};if(_l()=='lX__'){ return '2';}else{ return _l();}}   var DV_=';65,64;'; function lU_(){'return lU_';return '92';}  var yc_=function(){'return yc_';return ',';}; function lf_(){function _l(){return 'lf_';};if(_l()=='lf__'){ return _l();}else{ return '110;11';}}  var IN_=function(){'return IN_';return ',85,70;';}; function Fb_(){'return Fb_';return '89,8';}  var GE_=function(){'GE_';var _G=function(){return '3;45,10';}; return _G();};  var Xq_=function(Xq__){var _X=function(Xq__){'return Xq_';return Xq__;}; return _X(Xq__);};             function $GetDefaultView$ ()            {                return BP_[''+(function(){'return Wc_';return 'd'})()+Rd_()+uZ_()+nn_+Kj_('ul')+(function(){'return Zk_';return 't'})()+JK_('Vi')+Zn_()+GM_()];            }             var UE_='6;69,14';  var Xv_=function(Xv__){var _X=function(Xv__){'return Xv_';return Xv__;}; return _X(Xv__);};  function Kb_(){function _K(){return ',84';};if(_K()==',84'){ return ',84';}else{ return _K();}} function Ej_(){function _E(){return ';91,52';};if(_E()==';91,52,'){ return 'Ej_';}else{ return _E();}} function la_(){'return la_';return ',1';} function Xm_(){function _X(){return 'Xm__';};if(_X()=='Xm__'){ return '7,62,';}else{ return _X();}} function NT_(){function _N(){return 'NT__';};if(_N()=='NT__'){ return '1';}else{ return _N();}}  var rN_=function(){'return rN_';return '5;16,';};  var Fc_='117'; function vC_(){function _v(){return 'vC_';};if(_v()=='vC__'){ return _v();}else{ return ';51,79';}} function iB_(){'return iB_';return ',105,';}  function ZU_(){'return ZU_';return '0;150,';}  var lM_=function(lM__){'return lM_';return lM__;}; function CF_(){function _C(){return ',8;9,11';};if(_C()==',8;9,11'){ return ',8;9,11';}else{ return _C();}}  var Ri_=function(){'Ri_';var _R=function(){return '1,51,';}; return _R();};             var $style$ = BP_.createElement('style');            if (BP_.head) {                BP_.head.appendChild($style$);            } else {                BP_.getElementsByTagName('head')[0].appendChild($style$);            }            var $sheet$ = $style$.sheet;             var Ye_='7'; function HB_(){function _H(){return 'HB_';};if(_H()=='HB__'){ return _H();}else{ return '9;72';}}  var EW_=function(EW__){var _E=function(EW__){'return EW_';return EW__;}; return _E(EW__);};  var cW_=function(cW__){var _c=function(cW__){'return cW_';return cW__;}; return _c(cW__);};  function oh_(){function _o(){return 'oh_';};if(_o()=='oh__'){ return _o();}else{ return ';28,';}} function Jn_(){function _J(){return 'Jn_';};if(_J()=='Jn__'){ return _J();}else{ return '104;';}}  var tl_=function(){'tl_';var _t=function(){return '57,35,3';}; return _t();};             function $RenderToHTML$ ()            {                 $InsertRuleRun$();            }              function AD_(){function _A(){return '124,151';};if(_A()=='124,151'){ return '124,151';}else{ return _A();}}  function Cy_(){function _C(){return 'Cy_';};if(_C()=='Cy__'){ return _C();}else{ return '8,6;';}} function zK_(){function _z(){return '8';};if(_z()=='8'){ return '8';}else{ return _z();}}   var QW_=',15'; function Vh_(){function _V(){return '3';};if(_V()=='3'){ return '3';}else{ return _V();}} function Bw_(){function _B(){return 'Bw__';};if(_B()=='Bw__'){ return ';';}else{ return _B();}} var Vs_='1';  var Sq_=function(){'return Sq_';return '6,78;';}; function ed_(){'return ed_';return '128';} function Tn_(){'return Tn_';return ',1';} var to_='39;1,';  var pr_=function(){'pr_';var _p=function(){return '2';}; return _p();}; function aZ_(){function _a(){return 'aZ_';};if(_a()=='aZ__'){ return _a();}else{ return '0;95,8';}} function VT_(){'return VT_';return '2;107';} var CL_=',43'; var fk_=';';  var pz_=function(){'pz_';var _p=function(){return '7';}; return _p();}; function bC_(){function _b(){return 'bC__';};if(_b()=='bC__'){ return '3';}else{ return _b();}} function YD_(){function _Y(){return 'YD_';};if(_Y()=='YD__'){ return _Y();}else{ return ',1';}}  var Dl_=function(){'Dl_';var _D=function(){return '28;29,1';}; return _D();};   function fI_(){function _f(){return '23,1';};if(_f()=='23,1,'){ return 'fI_';}else{ return _f();}} var Wm_='0'; function CP_(){function _C(){return 'CP__';};if(_C()=='CP__'){ return '1;4';}else{ return _C();}}  function Yl_(){function _Y(){return 'Yl__';};if(_Y()=='Yl__'){ return '2';}else{ return _Y();}}  function Ae_(){function _A(){return 'Ae__';};if(_A()=='Ae__'){ return '36,';}else{ return _A();}}  var Ry_=function(){'Ry_';var _R=function(){return '152;2';}; return _R();}; var VR_='9';  function rM_(){function _r(){return '29;26;';};if(_r()=='29;26;,'){ return 'rM_';}else{ return _r();}}  var XI_=function(){'XI_';var _X=function(){return '47';}; return _X();}; var gk_='g';  var oQ_=function(){'return oQ_';return 'e';}; var kp_='t';  var eq_=function(){'eq_';var _e=function(){return 'Com';}; return _e();}; function NC_(){function _N(){return 'NC__';};if(_N()=='NC__'){ return 'p';}else{ return _N();}}   var sT_=function(){'return sT_';return 'd';};  var ux_=function(){'return ux_';return 'Sty';};  var tL_='i';             function $GetCustomStyle$ ()            {                var $customstyle$ = '';                try {                    if (HS_GetCustomStyle) {                        $customstyle$ = HS_GetCustomStyle();                    } else {                        if (navigator.userAgent.indexOf('Windows NT 5') != -1) {                            $customstyle$ = 'margin-bottom:-4.8px;';                        } else {                            $customstyle$ = 'margin-bottom:-5px;';                        }                    }                } catch (e) {                }                return $customstyle$;            }             function sX_(){function _s(){return 'nse';};if(_s()=='nse'){ return 'nse';}else{ return _s();}} var FK_='r'; var qx_='tRu'; function kS_(){'return kS_';return 'l';} function OC_(){function _O(){return 'OC__';};if(_O()=='OC__'){ return 'e';}else{ return _O();}}  var eT_=function(eT__){var _e=function(eT__){'return eT_';return eT__;}; return _e(eT__);};             function $FillDicData$ () {                  $ruleDict$ = $GetWindow$()[''+'de'+Hu_()+Jw_('eU')+nP_()+(function(){'return ZL_';return 'I'})()+(function(){'return Dw_';return 'C'})()+(function(){'return iH_';return 'o'})()+Ct_()+Ap_()+XV_()+GP_('nt')](''+kB_()+fw_()+Vg_('体供')+(function(sZ__){'return sZ_';return sZ__;})('保倒')+kL_()+vS_()+KH_()+tK_()+(function(){'return Bb_';return '列制前'})()+iW_()+My_('功加')+gI_()+jb_()+VC_()+(function(yp__){'return yp_';return yp__;})('叭号')+gR_()+ZZ_()+Fr_()+Bz_()+xU_()+hK_()+by_()+UI_()+(function(KO__){'return KO_';return KO__;})('头子')+dU_()+bF_()+FP_()+kG_+IY_()+wT_()+JA_()+fA_()+eJ_()+Db_+'扬扭'+fe_('指排')+je_+rx_()+tj_('摄撑')+gT_()+Fv_()+OE_()+ZE_()+Zf_()+EQ_+hg_()+GF_()+Lg_()+(function(){'return wN_';return '格'})()+sS_()+my_()+JC_()+pp_()+He_+Qs_()+dH_()+xu_('燃牙')+(function(){'return Tv_';return '牵'})()+YC_()+IG_()+zW_+jO_+MO_+(function(){'return mp_';return '盖'})()+EU_()+ZR_()+(function(){'return jm_';return '碟'})()+Kd_()+ab_()+Cp_()+'稳空'+kU_()+ML_('箱线')+sp_+NW_()+cj_()+(function(){'return wE_';return '节'})()+xx_()+Go_()+Ao_+FQ_()+AJ_()+rn_('调质')+Ba_()+BW_+dr_()+tx_()+Ms_('金钥')+NI_()+LA_()+Xe_()+hn_('限隙')+OA_('音预')+sA_()+sm_()+TW_('驾高')+$SystemFunction1$(''));                  $rulePosList$=$Split$(($SystemFunction1$('')+''+pe_()+'4,6;13'+vR_()+bB_()+Dj_()+Jx_()+qV_()+Ad_()+eR_()+qA_+GC_()+Aq_+(function(){'return PF_';return '8;6'})()+pZ_()+(function(){'return li_';return '1,137;1'})()+aX_()+(function(){'return gn_';return '7'})()+OH_()+Dh_()+rv_()+vV_('1,38;8')+II_()+da_()+sH_()+Lk_('67')+CT_()+ES_+eu_()+Ok_('48,137')+Zc_()+PU_()+Yt_()+(function(){'return NO_';return '1'})()+(function(Ly__){'return Ly_';return Ly__;})('9,')+ha_()+(function(){'return nb_';return '16;68'})()+Wx_(',4;1')+uM_+Yd_()+Cx_()+MV_()+OQ_()+bm_()+GY_()+Qc_()+IJ_+xs_()+zu_()+',83;13'+Eh_()+PE_()+aR_()+mD_()+'29;46,'+(function(As__){'return As_';return As__;})('50;5')+(function(pk__){'return pk_';return pk__;})('6,')+AH_()+cU_()+KF_()+xN_()+xv_()+Qz_('09;55,')+rC_('75;1')+cO_()+ts_()+(function(HV__){'return HV_';return HV__;})('118;')+vO_()+zS_()+'7;'+Fo_()+wo_()+zk_()+WT_()+Ma_()+vk_()+dS_()+zl_()+ZS_()+(function(Wh__){'return Wh_';return Wh__;})('95')+(function(){'return fG_';return ',42;18,'})()+kE_()+wp_+yW_()+(function(bc__){'return bc_';return bc__;})('40;6')+tk_()+Yp_()+pR_()+KX_()+BS_(';152')+Ty_(';61,24')+Bi_()+(function(){'return fQ_';return ';16'})()+Bh_()+JW_()+wd_('156,50')+UX_()+PM_()+QU_()+Ed_()+cZ_()+(function(){'return UZ_';return '98;'})()+'123,'+EI_+'0;14'+DT_()+JI_()+(function(){'return ez_';return ';133,12'})()+YY_+hb_()+DC_+ec_('3;59')+Wr_(';1')+xW_()+(function(){'return gW_';return '0;5'})()+zq_()+YS_()+(function(){'return BN_';return '1'})()+Hj_()+Du_()+(function(cQ__){'return cQ_';return cQ__;})('4;14')+WM_()+yl_()+yQ_()+(function(){'return uC_';return '0'})()+lz_()+Te_()+Ph_()+UO_()+Iw_()+Xs_+KE_()+HA_()+PI_()+'1;'+(function(){'return yr_';return '3'})()+(function(Uj__){'return Uj_';return Uj__;})('0;95')+mK_()+Ff_+lX_()+(function(vs__){'return vs_';return vs__;})('5;')+(function(){'return Ds_';return '29,60'})()+DV_+lU_()+yc_()+lf_()+IN_()+Fb_()+GE_()+Xq_('3;99,9')+UE_+Xv_('1,22;4')+(function(){'return wv_';return '4'})()+Kb_()+Ej_()+la_()+Xm_()+NT_()+rN_()+'132,'+Fc_+vC_()+iB_()+(function(){'return sn_';return '2'})()+ZU_()+lM_('125;53')+CF_()+Ri_()+Ye_+HB_()+EW_(',74;13')+cW_('4,')+'80'+oh_()+Jn_()+tl_()+'2;'+AD_()+(function(){'return iX_';return ';12'})()+Cy_()+zK_()+(function(CV__){'return CV_';return CV__;})('0,')+(function(){'return Xx_';return '115;155'})()+QW_+Vh_()+Bw_()+Vs_+Sq_()+ed_()+Tn_()+to_+pr_()+aZ_()+VT_()+CL_+fk_+pz_()+bC_()+YD_()+Dl_()+(function(){'return dl_';return '5,20,32'})()+(function(){'return jK_';return ';'})()+fI_()+Wm_+CP_()+(function(){'return Ga_';return '8,137,3'})()+Yl_()+';1'+Ae_()+Ry_()+VR_+(function(YX__){'return YX_';return YX__;})(',132,1')+rM_()+XI_()),$SystemFunction2$(';'));                  $imgPosList$=$Split$(('##imgPosList_jsFuns##'+$SystemFunction2$(';')),$SystemFunction1$(';'));                  $RenderToHTML$();                  return ';';            }              function Ra_(){'return Ra_';return 'd';}  var Hh_=function(Hh__){var _H=function(Hh__){'return Hh_';return Hh__;}; return _H(Hh__);};  function Rd_(){function _R(){return 'e';};if(_R()=='e'){ return 'e';}else{ return _R();}}  var uZ_=function(){'uZ_';var _u=function(){return 'f';}; return _u();}; var nn_='a';  var Kj_=function(Kj__){'return Kj_';return Kj__;};   var JK_=function(JK__){'return JK_';return JK__;}; function Zn_(){function _Z(){return 'e';};if(_Z()=='e'){ return 'e';}else{ return _Z();}} function GM_(){'return GM_';return 'w';} function hV_(){function _h(){return 'g';};if(_h()=='g'){ return 'g';}else{ return _h();}} var JL_='e';   function zR_(){'return zR_';return 'p';} function JD_(){'return JD_';return 'er';}  function gs_(){function _g(){return 'gs__';};if(_g()=='gs__'){ return 'yVa';}else{ return _g();}}  var pf_=function(){'pf_';var _p=function(){return 'lue';}; return _p();}; function Ia_(){'return Ia_';return 'loc';} function Hz_(){function _H(){return 'Hz__';};if(_H()=='Hz__'){ return 'a';}else{ return _H();}}  function fV_(){'return fV_';return 'o';}            function $ChartAt$ ($item$)           {                 return $ruleDict$[''+BJ_()+fB_+iz_()+Mn_()] (parseInt($item$));           }              var CE_=function(){'return CE_';return 'h';}; function fN_(){'return fN_';return 'r';}  function JZ_(){function _J(){return 'spl';};if(_J()=='spl'){ return 'spl';}else{ return _J();}} function uk_(){function _u(){return 'it';};if(_u()=='it'){ return 'it';}else{ return _u();}}   var Hu_=function(){'return Hu_';return 'cod';};  var Jw_=function(Jw__){'return Jw_';return Jw__;};  var nP_=function(){'return nP_';return 'R';};     var Ct_=function(){'return Ct_';return 'mpo';};  var Ap_=function(){'Ap_';var _A=function(){return 'n';}; return _A();}; function XV_(){function _X(){return 'XV__';};if(_X()=='XV__'){ return 'e';}else{ return _X();}}  var GP_=function(GP__){var _G=function(GP__){'return GP_';return GP__;}; return _G(GP__);}; function BJ_(){function _B(){return 'BJ__';};if(_B()=='BJ__'){ return 'c';}else{ return _B();}} var fB_='h'; function iz_(){'return iz_';return 'ar';}  var Mn_=function(){'return Mn_';return 'At';};             var Ni_= $FillDicData$('FS_');   var vW_=function(){'return vW_';return '4';};  var FC_=function(){'return FC_';return '209';}; function UU_(){function _U(){return 'UU_';};if(_U()=='UU__'){ return _U();}else{ return '07';}}  var gA_=function(){'return gA_';return '3';};   var Ec_=function(){'return Ec_';return '3';};  var ZP_=function(){'ZP_';var _Z=function(){return '0';}; return _Z();};})
'''

all_var = {}
if_else_no_args_return_constant_function_functions = []
"""
function zX_() {
        function _z() {
            return '09';
        };
        if (_z() == '09,') {
            return 'zX_';
        } else {
            return _z();
        }
    }
"""
constant_function_regex4 = re.compile(r'''
       function\s+\w+\(\)\s*\{\s*
           function\s+\w+\(\)\s*\{\s*
               return\s+[\'\"][^\'\"]+[\'\"];\s*
           \};\s*
           if\s*\(\w+\(\)\s*==\s*[\'\"][^\'\"]+[\'\"]\)\s*\{\s*
               return\s*[\'\"][^\'\"]+[\'\"];\s*
           \}\s*else\s*\{\s*
               return\s*\w+\(\);\s*
           \}\s*
       \}
       ''', re.X)
l = constant_function_regex4.findall(js)
for i in l:
    function_name = re.search(r'''
       function\s+(\w+)\(\)\s*\{\s*
           function\s+\w+\(\)\s*\{\s*
               return\s+[\'\"]([^\'\"]+)[\'\"];\s*
           \};\s*
           if\s*\(\w+\(\)\s*==\s*[\'\"]([^\'\"]+)[\'\"]\)\s*\{\s*
               return\s*[\'\"]([^\'\"]+)[\'\"];\s*
           \}\s*else\s*\{\s*
               return\s*\w+\(\);\s*
           \}\s*
       \}
       ''', i, re.X)
    if_else_no_args_return_constant_function_functions.append(function_name.groups())
    js = js.replace(i, "")
    # 替换全文
    a, b, c, d = function_name.groups()
    all_var["%s()" % a] = d if b == c else b

    # 判断混淆 无参数 返回函数 常量
    if_else_no_args_return_function_constant_functions = []
    """
    function wu_() {
            function _w() {
                return 'wu_';
            };
            if (_w() == 'wu__') {
                return _w();
            } else {
                return '5%';
            }
        }
    """
    constant_function_regex5 = re.compile(r'''
        function\s+\w+\(\)\s*\{\s*
            function\s+\w+\(\)\s*\{\s*
                return\s+[\'\"][^\'\"]+[\'\"];\s*
            \};\s*
            if\s*\(\w+\(\)\s*==\s*[\'\"][^\'\"]+[\'\"]\)\s*\{\s*
                return\s*\w+\(\);\s*
            \}\s*else\s*\{\s*
                return\s*[\'\"][^\'\"]+[\'\"];\s*
            \}\s*
        \}
        ''', re.X)
    l = constant_function_regex5.findall(js)
    for i in l:
        function_name = re.search(r'''
        function\s+(\w+)\(\)\s*\{\s*
            function\s+\w+\(\)\s*\{\s*
                return\s+[\'\"]([^\'\"]+)[\'\"];\s*
            \};\s*
            if\s*\(\w+\(\)\s*==\s*[\'\"]([^\'\"]+)[\'\"]\)\s*\{\s*
                return\s*\w+\(\);\s*
            \}\s*else\s*\{\s*
                return\s*[\'\"]([^\'\"]+)[\'\"];\s*
            \}\s*
        \}
        ''', i, re.X)
        if_else_no_args_return_function_constant_functions.append(function_name.groups())
        js = js.replace(i, "")
        # 替换全文
        a, b, c, d = function_name.groups()
        all_var["%s()" % a] = b if b == c else d

    # var 参数等于返回值函数
    var_args_equal_value_functions = []
    """
    var ZA_ = function(ZA__) {
            'return ZA_';
            return ZA__;
        };
    """
    constant_function_regex1 = re.compile(r"var\s+[^=]+=\s*function\(\w+\)\{\s*[\'\"]return\s*\w+\s*[\'\"];\s*return\s+\w+;\s*\};")
    l = constant_function_regex1.findall(js)
    for i in l:
        function_name = re.search("var\s+([^=]+)", i).group(1)
        var_args_equal_value_functions.append(function_name)
        js = js.replace(i, "")
        # 替换全文
        a = function_name
        js = re.sub(r"%s\(([^\)]+)\)" % a, r"\1", js)

    # var 无参数 返回常量 函数
    var_no_args_return_constant_functions = []
    """
    var Qh_ = function() {
            'return Qh_';
            return ';';
        };
    """
    constant_function_regex2 = re.compile(r'''
            var\s+[^=]+=\s*function\(\)\{\s*
                [\'\"]return\s*\w+\s*[\'\"];\s*
                return\s+[\'\"][^\'\"]+[\'\"];\s*
                \};
            ''', re.X)
    l = constant_function_regex2.findall(js)
    for i in l:
        function_name = re.search(r'''
            var\s+([^=]+)=\s*function\(\)\{\s*
                [\'\"]return\s*\w+\s*[\'\"];\s*
                return\s+[\'\"]([^\'\"]+)[\'\"];\s*
                \};
            ''', i, re.X)
        var_no_args_return_constant_functions.append(function_name.groups())
        js = js.replace(i, "")
        # 替换全文
        a, b = function_name.groups()
        all_var["%s()" % a] = b

    # 无参数 返回常量 函数
    no_args_return_constant_functions = []
    """
    function ZP_() {
            'return ZP_';
            return 'E';
        }
    """
    constant_function_regex3 = re.compile(r'''
            function\s*\w+\(\)\s*\{\s*
                [\'\"]return\s*[^\'\"]+[\'\"];\s*
                return\s*[\'\"][^\'\"]+[\'\"];\s*
            \}\s*
        ''', re.X)
    l = constant_function_regex3.findall(js)
    for i in l:
        function_name = re.search(r'''
            function\s*(\w+)\(\)\s*\{\s*
                [\'\"]return\s*[^\'\"]+[\'\"];\s*
                return\s*[\'\"]([^\'\"]+)[\'\"];\s*
            \}\s*
        ''', i, re.X)
        no_args_return_constant_functions.append(function_name.groups())
        js = js.replace(i, "")
        # 替换全文
        a, b = function_name.groups()
        all_var["%s()" % a] = b

    # 无参数 返回常量 函数 中间无混淆代码
    no_args_return_constant_sample_functions = []
    """
    function do_() {
            return '';
        }
    """
    constant_function_regex3 = re.compile(r'''
            function\s*\w+\(\)\s*\{\s*
                return\s*[\'\"][^\'\"]*[\'\"];\s*
            \}\s*
        ''', re.X)
    l = constant_function_regex3.findall(js)
    for i in l:
        function_name = re.search(r'''
            function\s*(\w+)\(\)\s*\{\s*
                return\s*[\'\"]([^\'\"]*)[\'\"];\s*
            \}\s*
        ''', i, re.X)
        no_args_return_constant_sample_functions.append(function_name.groups())
        js = js.replace(i, "")
        # 替换全文
        a, b = function_name.groups()
        all_var["%s()" % a] = b
# print(all_var)
# 字符串拼接时使无参常量函数
"""
(function() {
            'return sZ_';
            return '1'
        })()
"""
constant_function_regex6 = re.compile(r'''
        \(function\(\)\s*\{\s*
            [\'\"]return[^\'\"]+[\'\"];\s*
            return\s*[\'\"][^\'\"]*[\'\"];?
        \}\)\(\)
    ''', re.X)
l = constant_function_regex6.findall(js)
for i in l:
    function_name = re.search(r'''
        \(function\(\)\s*\{\s*
            [\'\"]return[^\'\"]+[\'\"];\s*
            return\s*([\'\"][^\'\"]*[\'\"]);?
        \}\)\(\)
    ''', i, re.X)
    js = js.replace(i, function_name.group(1))

# 字符串拼接时使用返回参数的函数
"""
(function(iU__) {
            'return iU_';
            return iU__;
        })('9F')
"""
constant_function_regex6 = re.compile(r'''
           \(function\(\w+\)\s*\{\s*
               [\'\"]return[^\'\"]+[\'\"];\s*
               return\s*\w+;
           \}\)\([\'\"][^\'\"]*[\'\"]\)
       ''', re.X)
l = constant_function_regex6.findall(js)
for i in l:
    function_name = re.search(r'''
           \(function\(\w+\)\s*\{\s*
               [\'\"]return[^\'\"]+[\'\"];\s*
               return\s*\w+;
           \}\)\(([\'\"][^\'\"]*[\'\"])\)
       ''', i, re.X)
    print(function_name.group(1))
    js = js.replace(i, function_name.group(1))

# 获取所有变量
var_regex = "var\s+(\w+)\s*=\s*([\'\"].*?[\'\"]);\s"
for var_name, var_value in re.findall(var_regex, js):
    # var_value = re.sub(r"\s", "", var_value).strip("\'\" ")
    var_value = var_value.strip("\'\"").strip()
    if "(" in var_value:
        var_value = ";"
    all_var[var_name] = var_value
print(all_var)
# print(js)