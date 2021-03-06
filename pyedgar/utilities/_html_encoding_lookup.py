#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

html_ent_re = re.compile('&[^; ]{1,10};')

def html_ent_re_sub_lambda(re_match):
    ent = re_match.group(0)
    
    if ent in HTML_ENCODE_LOOKUP:
        return HTML_ENCODE_LOOKUP[ent]
    return HTML_ENCODE_LOOKUP.get(ent.lower(), ent)

def html_ent_re_sub(text):
    return html_ent_re.sub(html_ent_re_sub_lambda, text)

HTML_ENCODE_LOOKUP = {
"&#0038;":'&amp;',
"&#0147;":'"',
"&#0148;":'"',
"&#0149;":'•',
"&#0151;":'—',
"&#0163;":'£',
"&#0201;":'É',
"&#0215;":'×',
"&#0228;":'ä',
"&#032;":' ',
"&#034;":'"',
"&#035;":'#',
"&#037;":'%',
"&#038;":'&amp;',
"&#039;":"'",
"&#040;":'(',
"&#041;":')',
"&#042;":'*',
"&#043;":'+',
"&#044;":',',
"&#045;":'-',
"&#0501;":'ǵ',
"&#0503;":'Ƿ',
"&#050;":'2',
"&#052;":'4',
"&#055;":'7',
"&#060;":'&lt;',
"&#061;":'=',
"&#062;":'&gt;',
"&#064;":'@',
"&#065;":'A',
"&#066;":'B',
"&#068;":'D',
"&#069;":'E',
"&#082;":'R',
"&#083;":'S',
"&#08804;":'≤',
"&#08805;":'≥',
"&#091;":'[',
"&#093;":']',
"&#094;":'^',
"&#095;":'_',
"&#096;":'`',
"&#098;":'b',
"&#0;":'',
"&#10003;":'✓',
"&#1028;":'Є',
"&#102;":'f',
"&#1040;":'A',
"&#1042;":'V',
"&#1052;":'M',
"&#1054;":'O',
"&#1056;":'R',
"&#1057;":'S',
"&#105;":'i',
"&#1072;":'a',
"&#1073;":'б',
"&#1077;":'e',
"&#1085;":'н',
"&#1086;":'o',
"&#1088;":'р',
"&#1089;":'с',
"&#108;":'l',
"&#1091;":'у',
"&#1093;":'х',
"&#10;":'\\n',
"&#110;":'n',
"&#111;":'o',
"&#113;":'q',
"&#115;":'s',
"&#116;":'t',
"&#117;":'u',
"&#118;":'v',
"&#119;":'w',
"&#11;":'',
"&#120;":'x',
"&#12288;":' ',
"&#12289;":', ',
"&#12298;":'&lt;&lt;',
"&#12299;":'&gt;&gt;',
"&#12356;":'i',
"&#12418;":'も',
"&#12424;":'よ',
"&#12475;":'セ',
"&#124;":'|',
"&#12521;":'ラ',
"&#12540;":'-',
"&#1254;":'Ӧ',
"&#125;":'}',
"&#127;":'',
"&#128;":'€',
"&#129;":'',
"&#130;":',',
"&#131;":'ƒ',
"&#132;":',,',
"&#133;":'...',
"&#134;":'†',
"&#135;":'‡',
"&#136;":'^',
"&#137;":'‰',
"&#138;":'Š',
"&#139;":'&lt;',
"&#13;":'\\n',
"&#140;":'Œ',
"&#142;":'Ž',
"&#143;":'',
"&#144;":'',
"&#145;":"'",
"&#146;":"'",
"&#147;":'"',
"&#148;":'"',
"&#149;":'•',
"&#14;":'',
"&#150;":'-',
"&#151;":'-',
"&#152;":'~',
"&#153;":'(tm)',
"&#154;":'š',
"&#155;":'&gt;',
"&#156;":'œ',
"&#157;":'',
"&#158;":'ž',
"&#159;":'Ÿ',
"&#15;":'',
"&#1606;":'ن',
"&#160;":' ',
"&#161;":'¡',
"&#162;":'¢',
"&#163;":'£',
"&#1649;":'ٱ',
"&#164;":'¤',
"&#165;":'¥',
"&#166;":'|',
"&#167;":'§',
"&#168;":'"',
"&#169;":'(c)',
"&#170;":'ª',
"&#171;":'&lt;&lt;',
"&#172;":'¬',
"&#173;":'-',
"&#174;":'(r)',
"&#175;":'-',
"&#176;":'°',
"&#177;":'±',
"&#178;":'²',
"&#179;":'³',
"&#180;":"'",
"&#181;":'µ',
"&#182;":'¶',
"&#183;":'·',
"&#184;":',',
"&#185;":'¹',
"&#186;":'º',
"&#187;":'&gt;&gt;',
"&#188;":'¼',
"&#189;":'½',
"&#190;":'¾',
"&#191;":'¿',
"&#192;":'À',
"&#193;":'Á',
"&#194;":'Â',
"&#195;":'Ã',
"&#196;":'Ä',
"&#197;":'Å',
"&#198;":'Æ',
"&#19978;":'上',
"&#199;":'Ç',
"&#200;":'È',
"&#20110;":'于',
"&#20140;":'京',
"&#20142;":'亮',
"&#201;":'É',
"&#20221;":'份',
"&#202;":'Ê',
"&#20399;":'侯',
"&#20445;":'保',
"&#204;":'Ì',
"&#20538;":'债',
"&#205;":'Í',
"&#206;":'Î',
"&#207;":'Ï',
"&#20822;":'兖',
"&#20844;":'公',
"&#20851;":'关',
"&#208;":'Ð',
"&#20975;":'凯',
"&#209;":'Ñ',
"&#21010;":'划',
"&#21046;":'制',
"&#210;":'Ò',
"&#211;":'Ó',
"&#212;":'Ô',
"&#213;":'Õ',
"&#21496;":'司',
"&#214;":'Ö',
"&#215;":'×',
"&#21672;":'咨',
"&#216;":'Ø',
"&#217;":'Ù',
"&#21839;":'問',
"&#21892;":'善',
"&#218;":'Ú',
"&#219;":'Û',
"&#220;":'Ü',
"&#221;":'Ý',
"&#22269;":'国',
"&#222;":'Þ',
"&#22323;":'圳',
"&#223;":'ß',
"&#224;":'à',
"&#225;":'á',
"&#22659;":'境',
"&#226;":'â',
"&#22791;":'备',
"&#227;":'ã',
"&#22806;":'外',
"&#22869;":'奕',
"&#228;":'ä',
"&#229;":'å',
"&#230;":'æ',
"&#231;":'ç',
"&#232;":'è',
"&#23391;":'孟',
"&#233;":'é',
"&#23425;":'宁',
"&#23436;":'完',
"&#23478;":'家',
"&#234;":'ê',
"&#235;":'ë',
"&#23616;":'局',
"&#236;":'ì',
"&#237;":'í',
"&#238;":'î',
"&#239;":'ï',
"&#24030;":'州',
"&#24037;":'工',
"&#240;":'ð',
"&#24191;":'广',
"&#24198;":'庆',
"&#241;":'ñ',
"&#24247;":'康',
"&#242;":'ò',
"&#24352;":'张',
"&#243;":'ó',
"&#244;":'ô',
"&#245;":'õ',
"&#246;":'ö',
"&#247;":'÷',
"&#248;":'ø',
"&#249;":'ù',
"&#250;":'ú',
"&#251;":'û',
"&#25216;":'技',
"&#252;":'ü',
"&#253;":'ý',
"&#254;":'þ',
"&#255;":'ÿ',
"&#256;":'Ā',
"&#257;":'ā',
"&#258;":'Ă',
"&#259;":'ă',
"&#25;":'',
"&#260;":'Ą',
"&#261;":'ą',
"&#26368;":'最',
"&#26377;":'有',
"&#263;":'ć',
"&#26415;":'术',
"&#26426;":'机',
"&#26472;":'杨',
"&#26800;":'械',
"&#268;":'Č',
"&#269;":'č',
"&#27056;":'榰',
"&#27154;":'樒',
"&#271;":'ď',
"&#274;":'Ē',
"&#275;":'ē',
"&#27719;":'汇',
"&#27974;":'浆',
"&#27982;":'济',
"&#279;":'ė',
"&#28023;":'海',
"&#28145;":'深',
"&#28165;":'清',
"&#281;":'ę',
"&#283;":'ě',
"&#28640;":'濠',
"&#28646;":'濦',
"&#287;":'ğ',
"&#28814;":'炎',
"&#29615;":'环',
"&#29702;":'理',
"&#29762;":'瑂',
"&#2;":'',
"&#30331;":'登',
"&#30340;":'的',
"&#304;":'İ',
"&#305;":'ı',
"&#30693;":'知',
"&#30;":'',
"&#31168;":'秀',
"&#31243;":'程',
"&#31649;":'管',
"&#318;":'ľ',
"&#322;":'ł',
"&#32440;":'纸',
"&#324;":'ń',
"&#327;":'Ň',
"&#328;":'ň',
"&#32929;":'股',
"&#32;":' ',
"&#333;":'ō',
"&#33406;":'艾',
"&#336;":'Ő',
"&#33775;":'華',
"&#337;":'ő',
"&#339;":'œ',
"&#341;":'ŕ',
"&#345;":'ř',
"&#346;":'Ś',
"&#347;":'ś',
"&#34;":'"',
"&#350;":'Ş',
"&#351;":'ş',
"&#35268;":'规',
"&#352;":'Š',
"&#353;":'š',
"&#355;":'ţ',
"&#35745;":'计',
"&#35774;":'设',
"&#357;":'ť',
"&#35810;":'询',
"&#360;":'Ũ',
"&#36731;":'轻',
"&#36890;":'通',
"&#368;":'Ű',
"&#369;":'ű',
"&#36;":'$',
"&#376;":'Ÿ',
"&#379;":'Ż',
"&#37;":'%',
"&#380;":'ż',
"&#382;":'ž',
"&#38382;":'问',
"&#38480;":'限',
"&#38;":'&amp;',
"&#39015;":'顧',
"&#39038;":'顾',
"&#39064;":'题',
"&#3913;":'ཉ',
"&#39;":"'",
"&#402;":'ƒ',
"&#4051;":'࿓',
"&#40;":'(',
"&#41;":')',
"&#42;":'*',
"&#43;":'+',
"&#44537;":'극',
"&#44;":',',
"&#45824;":'대',
"&#45;":'-',
"&#46020;":'도',
"&#478;":'Ǟ',
"&#47;":'/',
"&#48143;":'및',
"&#48;":'0',
"&#49440;":'선',
"&#49828;":'스',
"&#49884;":'시',
"&#49;":'1',
"&#505;":'ǹ',
"&#50808;":'외',
"&#50896;":'원',
"&#50;":'2',
"&#51201;":'적',
"&#51204;":'전',
"&#51;":'3',
"&#52264;":'차',
"&#52;":'4',
"&#53596;":'템',
"&#53;":'5',
"&#54252;":'포',
"&#54;":'6',
"&#55;":'7',
"&#56;":'8',
"&#57;":'9',
"&#58;":':',
"&#59450;":'',
"&#59;":';',
"&#60;":'<',
"&#61450;":'',
"&#61479;":'',
"&#61482;":'',
"&#61498;":'',
"&#61509;":'',
"&#61511;":'',
"&#61551;":'',
"&#61553;":'',
"&#61554;":'',
"&#61567;":'',
"&#61608;":'',
"&#61623;":'',
"&#61;":'=',
"&#62;":'&gt;',
"&#63;":'?',
"&#64257;":'fi',
"&#64336;":'ﭐ',
"&#64979;":'',
"&#64;":'@',
"&#65279;":'',
"&#65288;":'(',
"&#65289;":')',
"&#65293;":'-',
"&#65509;":'￥',
"&#65533;":'�',
"&#65;":'A',
"&#68;":'D',
"&#6;":'',
"&#706;":'&lt;',
"&#707;":'˃',
"&#710;":'^',
"&#769;":'',
"&#7778;":'Ṣ',
"&#7846;":'Ầ',
"&#7872;":'Ề',
"&#7913;":'ứ',
"&#7922;":'Ỳ',
"&#8057;":'ό',
"&#8194;":' ',
"&#8195;":' ',
"&#8203;":' ',
"&#8204;":' ',
"&#8206;":' ',
"&#8208;":'-',
"&#8209;":'-',
"&#8210;":'-',
"&#8211;":'-',
"&#8212;":'--',
"&#8213;":'--',
"&#8216;":"'",
"&#8217;":"'",
"&#8218;":',',
"&#8219;":"'",
"&#8220;":'"',
"&#8221;":'"',
"&#8222;":',,',
"&#8223;":'"',
"&#8224;":'†',
"&#8225;":'‡',
"&#8226;":'•',
"&#8230;":'…',
"&#8232;":'\\n',
"&#8234;":'',
"&#8236;":'',
"&#8240;":'‰',
"&#8242;":"'",
"&#8243;":'',
"&#8249;":'&lt;',
"&#8260;":'/',
"&#8298;":'-',
"&#8301;":"'",
"&#8303;":"'",
"&#8355;":'₣',
"&#8356;":'₤',
"&#8361;":'₩',
"&#8364;":'€',
"&#8369;":'₱',
"&#83;":'S',
"&#8414;":'',
"&#8453;":'℅',
"&#8482;":'(tm)',
"&#84;":'T',
"&#8531;":'⅓',
"&#8532;":'⅔',
"&#8539;":'⅛',
"&#8540;":'⅜',
"&#8541;":'⅝',
"&#8542;":'⅞',
"&#8594;":'→',
"&#8595;":'↓',
"&#8710;":'∆',
"&#8721;":'∑',
"&#8722;":'-',
"&#8727;":'*',
"&#8729;":'∙',
"&#8730;":'√',
"&#8734;":'∞',
"&#8776;":'≈',
"&#8804;":'≤',
"&#8805;":'≥',
"&#8806;":'≦',
"&#894;":';',
"&#8;":'',
"&#900;":"'",
"&#914;":'B',
"&#916;":'Δ',
"&#91;":'[',
"&#931;":'Σ',
"&#93;":']',
"&#945;":'α',
"&#946;":'β',
"&#9472;":'-',
"&#9474;":'|',
"&#947;":'γ',
"&#948;":'δ',
"&#949;":'ε',
"&#950;":'ζ',
"&#9552;":'=',
"&#95;":'_',
"&#9608;":'█',
"&#9632;":'■',
"&#9633;":'□',
"&#9642;":'▪',
"&#9658;":'►',
"&#9675;":'○',
"&#9679;":'●',
"&#9702;":'◦',
"&#971;":'ϋ',
"&#972;":'ό',
"&#9744;":'☐',
"&#9745;":'☑',
"&#9830;":'♦',
"&#98;":'b',
"&#9;":'\\t',
"&#x105;":'ą',
"&#x107;":'ć',
"&#x10D;":'č',
"&#x10d;":'č',
"&#x142;":'ł',
"&#x15B;":'ś',
"&#x15b;":'ś',
"&#x17C;":'ż',
"&#x17c;":'ż',
"&#x2011;":'-',
"&#x2013;":'-',
"&#x2014;":'--',
"&#x2018;":"'",
"&#x2019;":"'",
"&#x201C;":'"',
"&#x201c;":'"',
"&#x201D;":'"',
"&#x201d;":'"',
"&#x2022;":'•',
"&#x2026;":'…',
"&#x20AC;":'€',
"&#x20ac;":'€',
"&#x2122;":'(tm)',
"&#x2154;":'⅔',
"&#x215B;":'⅛',
"&#x215b;":'⅛',
"&#x2264;":'≤',
"&#x2265;":'≥',
"&#x25CF;":'●',
"&#x25cf;":'●',
"&#x25FB;":'◻',
"&#x25fb;":'◻',
"&#x2610;":'☐',
"&#x2611;":'☑',
"&#x2612;":'☒',
"&#x85;":'…',
"&#x86;":'†',
"&#x8c;":'Œ',
"&#x9e;":'ž',
"&#x9f;":'Ÿ',
"&#xA0;":' ',
"&#xA3;":'£',
"&#xa3;":'£',
"&#xA5;":'¥',
"&#xa5;":'¥',
"&#xA7;":'§',
"&#xa7;":'§',
"&#xA8;":'"',
"&#xa8;":'"',
"&#xA9;":'(c)',
"&#xa9;":'(c)',
"&#xAC;":'¬',
"&#xac;":'¬',
"&#xAD;":'-',
"&#xad;":'-',
"&#xAE;":'(r)',
"&#xae;":'(r)',
"&#xB0;":'°',
"&#xb0;":'°',
"&#xB7;":'·',
"&#xb7;":'·',
"&#xBC;":'¼',
"&#xbc;":'¼',
"&#xBD;":'½',
"&#xbd;":'½',
"&#xC9;":'É',
"&#xc9;":'É',
"&#xDF;":'ß',
"&#xdf;":'ß',
"&#xE0;":'à',
"&#xe0;":'à',
"&#xE1;":'á',
"&#xe1;":'á',
"&#xE4;":'ä',
"&#xe4;":'ä',
"&#xE8;":'è',
"&#xe8;":'è',
"&#xE9;":'é',
"&#xe9;":'é',
"&#xED;":'í',
"&#xed;":'í',
"&#xF020;":'',
"&#xf020;":'',
"&#xF06F;":'',
"&#xf06f;":'',
"&#xF0B7;":'',
"&#xf0b7;":'',
"&#xF0B8;":'',
"&#xf0b8;":'',
"&#xF3;":'ó',
"&#xf3;":'ó',
"&#xF6;":'ö',
"&#xf6;":'ö',
"&#xF7;":'÷',
"&#xf7;":'÷',
"&#xFC;":'ü',
"&#xfc;":'ü',
"&#xFE;":'þ',
"&#xfe;":'þ',
"&#xa0;":' ',
"&Aacute;":'Á',
"&Acirc;":'Â',
"&Agrave;":'À',
"&Aring;":'Å',
"&Atilde;":'Ã',
"&Auml;":'Ä',
"&Ccedil;":'Ç',
"&Delta;":'Δ',
"&delta;":'Δ',
"&Eacute;":'É',
"&Ecirc;":'Ê',
"&Egrave;":'È',
"&Euml;":'Ë',
"&Iacute;":'Í',
"&Igrave;":'Ì',
"&Ntilde;":'Ñ',
"&Oacute;":'Ó',
"&Ocirc;":'Ô',
"&Oslash;":'Ø',
"&Otilde;":'Õ',
"&Ouml;":'Ö',
"&Uacute;":'Ú',
"&Ucirc;":'Û',
"&Uuml;":'Ü',
"&aacute;":'á',
"&acirc;":'â',
"&acute;":"'",
"&aelig;":'æ',
"&agrave;":'à',
"&aring;":'å',
"&asymp;":'≈',
"&atilde;":'ã',
"&auml;":'ä',
"&bdquo;":',,',
"&bull;":'•',
"&ccedil;":'ç',
"&cedil;":'¸',
"&cent;":'¢',
"&copy;":'(c)',
"&dagger;":'†',
"&deg;":'°',
"&diams;":'♦',
"&divide;":'÷',
"&eacute;":'é',
"&ecirc;":'ê',
"&egrave;":'è',
"&emsp;":' ',
"&eth;":'ð',
"&euml;":'ë',
"&euro;":'€',
"&frac12;":'½',
"&frac14;":'¼',
"&frac34;":'¾',
"&ge;":'≥',
"&half;":'½',
"&hellip;":'…',
"&iacute;":'í',
"&icirc;":'î',
"&iexcl;":'¡',
"&igrave;":'ì',
"&iquest;":'¿',
"&iuml;":'ï',
"&laquo;":'&lt;&lt;',
"&ldquo;":'"',
"&le;":'≤',
"&lrm;":'\\u200e',
"&lsaquo;":'&lt;',
"&lsquo;":"'",
"&mdash;":'--',
"&middot;":'·',
"&minus;":'-',
"&nbsp;":' ',
"&ndash;":'-',
"&not;":'¬',
"&ntilde;":'ñ',
"&oacute;":'ó',
"&ocirc;":'ô',
"&ograve;":'ò',
"&ordf;":'ª',
"&ordm;":'º',
"&oslash;":'ø',
"&otilde;":'õ',
"&ouml;":'ö',
"&para;":'¶',
"&plusmn;":'±',
"&pound;":'£',
"&quot;":'"',
"&radic;":'√',
"&raquo;":'&gt;&gt;',
"&rdquo;":'"',
"&reg;":'(r)',
"&rsquo;":"'",
"&sect;":'§',
"&shy;":'-',
"&sup1;":'¹',
"&sup2;":'²',
"&sup3;":'³',
"&szlig;":'ß',
"&thinsp;":' ',
"&thorn;":'þ',
"&times;":'×',
"&trade;":'(tm)',
"&uacute;":'ú',
"&ucirc;":'û',
"&ugrave;":'ù',
"&uml;":'"',
"&uuml;":'ü',
"&yacute;":'ý',
"&yen;":'¥',
"&yuml;":'ÿ',
}
