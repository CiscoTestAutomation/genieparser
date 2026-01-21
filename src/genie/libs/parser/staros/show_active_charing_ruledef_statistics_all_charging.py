"""starOS implementation of show temperature.py

"""
from os import stat_result
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Schema

class ShowACSchema(MetaParser):
    """Schema for show active-charging ruledef statistics all charging"""

    schema = {
        'ac_table': {
            Any():{
                'PACKETS_DOWN': str,
                'BYTES_DOWN': str,
                'PACKETS_UP': str,
                'BYTES_UP': str,
                'HITS': str,
                'MATCH': str,
                },
            'Summary':{
                'TOTAL': str,
            },
        },
    }    
    """
            'Summary':{
                'TOTAL': str,
            },

    """

class ShowAC(ShowACSchema):
    """Parser for show active-charging ruledef statistics all charging"""

    cli_command = 'show active-charging ruledef statistics all charging'

    """
[local]ASU-ASR5K5-1# show active-charging ruledef statistics all charging
Friday December 22 20:54:18 ART 2023

Ruledef Name        Packets-Down  Bytes-Down  Packets-Up   Bytes-Up       Hits Match-Bypassed
------------        ------------  ----------  ----------   --------       ---- --------------
AUP-ALL-1Luis            892035245744 974546321120052 368889466072 95248711956718 1223093338260      147610659
AUP-ALL-TETH-1         718493638 714052238036   409607331 87186689740 1104073641            266
AUP-ALL_HTTP-1           5374442   319667816    13737843 1937516143    4516311              0
AUP-CLARO-AUTOGESTION-1             0           0           0          0          0              0
AUP-CLARO-CONTENEDOR-1       9656237  3175329040    11288869 4691355927   19415957              0
AUP-CLARO-IDEAS                0           0          17        972         10              0
AUP-CLARO-IDEAS-4              0           0           0          0          0              0
AUP-CLARO-INTRA-1          23358    29427833       10713    1029208      33397              0
AUP-CLARO_APP_CAC-2             0           0           0          0          0              0
AUP-CLARO_MI-4                 0           0           0          0          0              0
AUP-CLARO_MUSICA-1       8500435 10259987593     4879595  438285802   12990862              0
AUP-CLARO_MUSICA-13       2304765  3104446158      988536   75743706    3284379              0
AUP-CLARO_MUSICA-14          1917     2164055        1662     114980       3362              0
AUP-CLARO_MUSICA-16       3115096  3561026131     1393721  190809552    4311773              0
AUP-CLARO_MUSICA-18       4678368  5826883277     2148659  210712334    6656379              0
AUP-CLARO_MUSICA-19       4204897  5796395608     1181153   69473019    5371395              0
AUP-CLARO_MUSICA-2             0           0           0          0          0              0
AUP-CLARO_MUSICA-20             0           0           0          0          0              0
AUP-CLARO_MUSICA-21             0           0           0          0          0              0
AUP-CLARO_MUSICA-26          2786     3322693        2314     226725       4910              0
AUP-CLARO_MUSICA-27           181       70479         205      25128        338              0
AUP-CLARO_MUSICA-28          2556     1034495        2388     375711       4339              0
AUP-CLARO_MUSICA-3             0           0           0          0          0              0
AUP-CLARO_MUSICA-31             0           0           0          0          0              0
AUP-CLARO_MUSICA-32          9138     5472909        9082    1477054      15240              0
AUP-CLARO_MUSICA-33             0           0           0          0          0              0
AUP-CLARO_MUSICA-35          3882     3940243        3494     276706       6619              0
AUP-CLARO_MUSICA-36             0           0           0          0          0              0
AUP-CLARO_MUSICA-4             0           0           0          0          0              0
AUP-CLARO_MUSICA-51          1548      244177        2098     374851       2979              0
AUP-CLARO_MUSICA-61        612978   517656452      478718   63333619     995349              0
AUP-CLARO_MUSICA-76             0           0           0          0          0              0
AUP-CLARO_MUSICA-78             0           0           0          0          0              0
AUP-CLARO_MUSICA-82             0           0           0          0          0              0
AUP-CLARO_MUSICA-86         51392    41538519       38685    5392385      82272              0
AUP-CLARO_MUSICA-88             0           0           0          0          0              0
AUP-CLARO_MUSICA-89          2002      446630        2893     602076       3524              0
AUP-CLARO_MUSICA-90           268      116809         266      57892        466              0
AUP-CLARO_S1GATEWAY-2        103065    86921452       93953   42554019     188256              0
AUP-CLARO_S1GATEWAY-4         96376    86448691       78043   22992434     165817              0
AUP-COTA-1-ESIM          5116391  1627077436     5339554 2233642304    9714065              0
AUP-COTA-2-ESIM            12836    13693196        9189     784349      20995              0
AUP-DATAMI-1                  12         720           8        420          4              0
AUP-DATAMI-2                   0           0           0          0          0              0
AUP-DATAMI-3              183182   254027847      160504    8531618     342918              0
AUP-DTIGNITE-1               971      488343        1319     189878       1925              0
AUP-DTIGNITE-2                11        5429          16       2914         23              0
AUP-DTIGNITE-4          14389383 18674103769     4627822  756501542   18800472              0
AUP-DTIGNITE-7          14496993 20016211686     5120216  282130351   19612220              0
AUP-FACEBOOK-AF                0           0           0          0          0              0
AUP-FACEBOOK-AF-2        2167410   129994375     6055698  967319941    1975312              0
AUP-FB-FREE-1         5234026628 2163777247230  5055398428 1001961630303 9234370503              0
AUP-FB-FREE-HE-1-IP      41280113  7316500870    44745188 5521204360   61790906              0
AUP-FB-SP-1           7588409989 8438894654988  2328316127 534259023174 9786352259              0
AUP-FREE-FIRE-CDN       40473387 55194645425    17404500 1085693232   57643957              0
AUP-FREE-FIRE-LOAD-BALANCER           672      375094         823     353271       1460              0
AUP-FREE-FIRE-PLATFORM-SERVER           326      277681         200      15321        502              0
AUP-FREE-FIRE-SAC-GAME-SERVER      16936333  2228534201    14424076 1360218626   31322824              0
AUP-FREE-FIRE-SAC-REGION-SERVER             0           0          67       5628         67              0
AUP-FREE-FIRE-VOICE-SERVER    1003386857 78559442181   536882996 42982966611 1537440948              0
AUP-GAMELOFT-1           1789167  2250039701     1012924   83037870    2679425              0
AUP-GAMELOFT-10           233420   203416591      183927   17898189     394049              0
AUP-GAMELOFT-11              956      127673        1229     117785       1551              0
AUP-GAMELOFT-12               42       23080          50       7578         80              0
AUP-GAMELOFT-2           8620052  8103190437     7649774 1002160233   15205810              0
AUP-GAMELOFT-3                 0           0           0          0          0              0
AUP-GAMELOFT-5                 0           0           0          0          0              0
AUP-GAMELOFT-6            449624   588032024      273670   16905485     694556              0
AUP-GAMELOFT-7             44576    41372895       39913    5538656      77508              0
AUP-GAMELOFT-8             14543    17080196       16375    1166356      29676              0
AUP-GAMELOFT-9             92725   108434876       77549    9013661     163432              0
AUP-GEOLOCALIZACION-1             0           0           0          0          0              0
AUP-GM-FOTA-1           31313482 43274740144    13510544  750599994   44782716              0
AUP-GM-FOTA-2                  0           0           0          0          0              0
AUP-GM-FOTA-3           17981944 24954205724     8337059  447701452   26317545              0
AUP-GM-FOTA-4             969086  1285668867      609104   44605695    1570826              0
AUP-GM-GRANEL-1         62521407 27508830849    66231044 15141010812  112628268              0
AUP-GM-GRANEL-10               0           0           0          0          0              0
AUP-GM-GRANEL-11               0           0           0          0          0              0
AUP-GM-GRANEL-13               0           0           0          0          0              0
AUP-GM-GRANEL-14               0           0           0          0          0              0
AUP-GM-GRANEL-15         1090660   544079121      994807  203934917    1672752              0
AUP-GM-GRANEL-2         47372830 65410352059    15715640  857934189   63044247              0
AUP-GM-GRANEL-3                0           0           0          0          0              0
AUP-GM-GRANEL-4              180       54654         183      16203        331              0
AUP-GM-GRANEL-5                0           0           0          0          0              0
AUP-GM-GRANEL-6                0           0           0          0          0              0
AUP-GM-GRANEL-7         28279233 11657156747    35976239 11559187467   56533338              0
AUP-GM-GRANEL-8         50684901 20728358726    61127414 15519407130   97287962              0
AUP-GM-GRANEL-9            17084    18342341       12148     850633      28583              0
AUP-GM-I-1                     0           0           0          0          0              0
AUP-GM-I-2                     0           0           0          0          0              0
AUP-GM-I-3                     0           0           0          0          0              0
AUP-GM-I-4                     0           0           0          0          0              0
AUP-GM-I-6                     0           0           0          0          0              0
AUP-GM-I-7                     0           0           0          0          0              0
AUP-GOOGLE-DNS-1              16         983          20       1007         24              0
AUP-GOOGLE-DNS-2               0           0           0          0          0              0
AUP-GOOGLE-PLAY-P2P-1   14361057287 18092297959945  2824012326 275704681097 17106014115              0
AUP-GOOGLE-RCS-1      1041233283 392126414162  1013912804 419893729337 2011379529              0
AUP-INSTAGRAM-1        360694079 210723211157   320618777 213338336818  672070346              0
AUP-INSTAGRAM-1-TLS-SNI        214215    86246848      203999   68285478     364604              0
AUP-INSTAGRAM-2         15122105 10362078735    11419652 7351776307   26190082              0
AUP-INSTAGRAM-3        170194051 83945221751   135190829 40386312590  278130185              0
AUP-INSTAGRAM-3-TLS-SNI     308940928 117939984869   315137239 73275379233  567719292              0
AUP-INSTAGRAM-4          1576669  1547966279      883342  118925213    2383697              0
AUP-INSTAGRAM-4-TLS-SNI        444358   495072615      313597   25010598     727807              0
AUP-INSTAGRAM-5       7182257818 8778791843246  1005398159 107400251383 8177608204              0
AUP-INSTAGRAM-P2P-1     227367298 220880316141   154591409 24975406827  358153131              0
AUP-MEDALLIA                   3         300           5        621          5              0
AUP-MMS-1                      0           0           0          0          0              0
AUP-MMS-5                  16923     1000412       22601   27233348      37657              0
AUP-MMS-6                  71929    87108514       54998    6489297     119333              0
AUP-PORTAL-REDIRECT-1      17071563  1024545548    44113338 5321656006   14448357              0
AUP-PORTAL-SHOP-HTTP-1             0           0           0          0          0              0
AUP-PORTAL-SHOP-HTTP-2             0           0           0          0          0              0
AUP-PORTAL-SHOP-HTTPS-2             0           0           0          0          0              0
AUP-PORTAL-SHOP-HTTPS-4             0           0           0          0          0              0
AUP-PORTAL_APRENDE-1         33326    43866671       20961    1686613      53653              0
AUP-PSIPHON-BLOCK       13741815  4936607226    19552348 2941141838   25869627          53267
AUP-SAMSUNG-SINGLE       8594384 11965628954     2491915  145815791   11085681              0
AUP-SM-SR                  28321     3990661       33425    5193327      54161              0
AUP-SMART-ADSERVER-1             0           0           0          0          0              0
AUP-SMART-ADSERVER-2             0           0           0          0          0              0
AUP-SMART-ADSERVER-3           186       21291         333      59187        397              0
AUP-SMART-ADSERVER-4             0           0           0          0          0              0
AUP-SPEEDY-MOVIL-10             0           0        2291     137460        436              0
AUP-SPEEDY-MOVIL-11         30969    24853413       51773    5447918      69933              0
AUP-SPEEDY-MOVIL-13       3376682  1829706436     5186953  441080541    6211048              0
AUP-SPEEDY-MOVIL-15             0           0           0          0          0              0
AUP-SPEEDY-MOVIL-16          6949     1674016       12719    1465878      13594              0
AUP-SPEEDY-MOVIL-17             0           0           0          0          0              0
AUP-SPEEDY-MOVIL-18        709781   199879991     1285547  278398024    1489438              0
AUP-SPEEDY-MOVIL-23             0           0           0          0          0              0
AUP-SPEEDY-MOVIL-6             0           0        1001      60060        169              0
AUP-SPEEDY-MOVIL-7             0           0           0          0          0              0
AUP-TIKTOK-1          6420997542 7965156381018  2980728649 386804729387 9148220504           2582
AUP-TIKTOK-2             4101239  5513817840     1910796  143696049    5959372              0
AUP-TWITTER-1             118668    17384481      175067   14306051     120274              0
AUP-TWITTER-1-TLS-SNI           187       39017         186      39602        306              0
AUP-TWITTER-13            198964    71791807      209515   45993846     382273              0
AUP-TWITTER-14              3133     4055548        2212     151095       5285              0
AUP-TWITTER-15          28638650 36928568097    16432015 1103465338   44306113              0
AUP-TWITTER-2            2141587  2422510834     1282117  149186702    3337671              0
AUP-TWITTER-3                  0           0           0          0          0              0
AUP-TWITTER-3-TLS-SNI             0           0           0          0          0              0
AUP-TWITTER-4             114108   104290305       90510    6946367     154653              0
AUP-TWITTER-5                 14        1078          19       1580         22              0
AUP-TWITTER-5-TLS-SNI          1125      427754        1131     123561       2044              0
AUP-TWITTER-6                  0           0           0          0          0              0
AUP-TWITTER-7                  0           0           0          0          0              0
AUP-TWITTER-9                  0           0           0          0          0              0
AUP-TWITTER-P2P-1      169265702 195842644352    85758465 10734854588  249981967              0
AUP-VANTIO-1              127391    23940804      150488    9181067     191992              0
AUP-VANTIO-2           979057456 164315934748  1425202575 95639297179 2404260029              0
AUP-VANTIO-3                   0           0           0          0          0              0
AUP-VANTIO-4              112695    15591861      126246    7872713     238941              0
AUP-VANTIO-5                   0           0           0          0          0              0
AUP-VANTIO-6                   0           0           0          0          0              0
AUP-VANTIO-7             1961006   368293072     2367279  142076802    3075184              0
AUP-VANTIO-8          5664723016 977327715000  6237387882 432001920296 11902110892              0
AUP-VPN-1               93558308 72081973859    73745510 9973339173  162706610              0
AUP-WHATSAPP-1      177913057484 214194333255907 76214556599 17861543169505 251489130473              0
AUP-YOUTUBE-1-TLS-SNI             0           0           0          0          0              0
AUP-YOUTUBE-10         303848943 226758752410   293290745 202090570646  597139372              0
AUP-YOUTUBE-11           1397404   911269413     1425374  463443784    2822778              0
AUP-YOUTUBE-12            109333   102491700       56629   13489721     165962              0
AUP-YOUTUBE-13           4579501  5311060078     1932423  295517218    6511924              0
AUP-YOUTUBE-14          13044214 14961475399     5305703  860215690   18349917              0
AUP-YOUTUBE-15          12375741  6875348916     9182478 2321842137   21558219              0
AUP-YOUTUBE-16                90       54045          84      30259        174              0
AUP-YOUTUBE-17           1873442   906563928     1711321  519823391    3584763              0
AUP-YOUTUBE-18           2733866   966925333     2439742  549009927    5173608              0
AUP-YOUTUBE-19             70748    38551073       62358   20453486     133106              0
AUP-YOUTUBE-2-TLS-SNI          3779     2732794        2400     308941       4898              0
AUP-YOUTUBE-20          24369231 18065109399    17748144 5579094667   42117359              0
AUP-YOUTUBE-21        1964251971 2401842702968   404197490 65604331082 2365375105              0
AUP-YOUTUBE-22          34177006 36376094599    14413409 2170227690   48008084              0
AUP-YOUTUBE-23          92062859 99967165601    38072329 4855698592  127105443              0
AUP-YOUTUBE-24         232537714 139324571688   202968869 62219726205  412581446              0
AUP-YOUTUBE-25         874549193 424851695909   866172863 439700746254 1621100398              0
AUP-YOUTUBE-26           1914266  2221996735      975733  162900245    2889999              0
AUP-YOUTUBE-27           3752689  2353856366     3747509 1394997490    7500198              0
AUP-YOUTUBE-29                 0           0           0          0          0              0
AUP-YOUTUBE-30               485      234377         517     114356       1002              0
AUP-YOUTUBE-4-TLS-SNI          2000     1433660        1295     154476       2499              0
AUP-YOUTUBE-5-TLS-SNI          3189     3776660        1785     161335       4697              0
AUP-YOUTUBE-6             224265   146414733      223365   74360620     447630              0
AUP-YOUTUBE-7           57556895 58796438973    27660449 5768423118   85217335              0
AUP-YOUTUBE-8            7068892  5118038079     6366289 2360819785   13435181              0
AUP-YOUTUBE-9            7757311  4539064370     7039727 3440738932   14797038              0
AUP-YOUTUBE-P2P-1     3140294281 3814725846358  1055931563 173582379501 4155811206              0
PY-AUTOGESTION-1               0           0        1602      97020        266              0
PY-BLOCK                  365664    16749362     2233407  124279058    1409464              0
PY-BLUE_MOVIL-1             2307     2751998        2236     194024       4331              0
PY-BLUE_MOVIL-2              166      132364         223      38634        346              0
PY-CENSO-1-2022           269308   364582082      190536   10591911     456900              0
PY-CENSO-2-2022           630653   855874740      287165   20944405     910762              0
PY-CENSO-3-2022           472329   639805172      261329   26219828     731046              0
PY-CIBERSONS-1                 0           0           0          0          0              0
PY-CLARO-1                 77144    46991508       77833    7015035     107175              0
PY-CLARO-ABM-1              3843     1337969      512235   31348223      93761              0
PY-CLARO-CLUB-1            29747     5305497       35081    8387349      48755              0
PY-CLARO-CLUB-4           113962    42113476      133901   25887481     211652              0
PY-CLARO-DOC-AUTOGESTION-1           843      411294       72670    5010773      14474              0
PY-CLARO-EMPRESAS-1            35        1860        6422     386208       1144              0
PY-CLARO-IDEAS-1          268825   299588330      135219   12978932     395513              0
PY-CLARO-IDEAS-2          538655   503744792      326413   41604519     844126              0
PY-CLARO-IDEAS-3          116429   118358423       61587    7151313     174103              0
PY-CLARO-PORTALCOMPRAS-2        336701    72528173      384234  123375980     565117              0
PY-CLARO-PORTALCOMPRAS-4        561234   474138149     6809909  464185015    1980883              0
PY-CLARO-SVA-1            150305    25162358      212891   23938564     207279              0
PY-CLAROCLUBAPPS-5       1108592  1331483238      436293   73142373    1538625              0
PY-CLAROVIDEO-1          5652425  7198920605     3021385  257354199    8529765              0
PY-CLARO_GIROSPDG-1             7         420        2024     119612        388              0
PY-CLARO_INDIVIDUOS-1             0           0           0          0          0              0
PY-CLARO_PORTAL-1              0           0           0          0          0              0
PY-CLARO_PORTAL-3          92381    91802688      146882   10829606     146962              0
PY-CLARO_PORTAL-4              0           0          12        720          2              0
PY-CLARO_PORTAL-5          18187    20679942       12479    1178236      29931              0
PY-CLARO_PORTAL-7            908      358770      130666    7886658      24767              0
PY-CLARO_PORTALCOMERCIO-1          1925      463215      168958   10203695      32995              0
PY-CLARO_PORTAL_DNSSNI-1        245096   148215611      284812   31775897     436610              0
PY-CLARO_PORTAL_DNSSNI-2      86552112 90716828043    56389742 9979687806  139401869              0
PY-CLARO_PORTAL_FREE-NO-URI-1       1076868   131673612     1300748  225711307    1726476              0
PY-CLARO_PORTAL_FREE-NO-URI-2       2397960  1417751961     2197460  714227646    3940694              0
PY-CLARO_S1GATEWAY-1         89841    48837102       95281   79698527     182584              0
PY-CLARO_SUBSIDIOS-1           214      183189         192      17002        376              0
PY-CLARO_TIENDA-1          16638    15451613       15887    1909602      25666              0
PY-CLARO_VIAJES-1              0           0           0          0          0              0
PY-FUNMOVILCLUB-1              8         448          10        536          8              0
PY-GOOGLE-RCS-6           761935   225201003      831648   80014607    1091420              0
PY-HACIENDA-1                  0           0         392      23740         56              0
PY-INTERNETQ                  10         929          18       7198         22              0
PY-LOGMEIN-1                   0           0           0          0          0              0
PY-MDI-1                       0           0        2994     369104       2994              0
PY-MEC-1                31782660 39197089065    16242176 2472539559   47354782              0
PY-MICLARO-1                  22        1288       14947    1022348       2601              0
PY-MMSL-2                    680       34768         765     696231       1246              0
PY-MOVICLIPS-1                 0           0           0          0          0              0
PY-MSP-BS                8891718 11658054216     6924445  494094875   15679884              0
PY-MUSICA_STORE-1              0           0         217      13020         57              0
PY-OPRATEL-2                   0           0           0          0          0              0
PY-OPRATEL-3                1060     1017892        1060     202962       1941              0
PY-OPRATEL-HE-1                5         836           6        863          8              0
PY-OTA-1                     958       96700        1260     119700       1903              0
PY-PLAYTOWN-1             465188   135318705      509693  148778737     762311              0
PY-PORTAL-SHOP-HTTP-HE-ENCRYPTED_1             0           0           0          0          0              0
PY-PORTAL-SHOP-HTTP-HE-ENCRYPTED_2             0           0           0          0          0              0
PY-PORTAL-SHOP-HTTP-HE-ENCRYPTED_DESARROLLO             0           0           0          0          0              0
PY-PORTAL-SHOP-HTTPS-1             0           0           0          0          0              0
PY-PORTAL-SHOP-HTTPS-3             0           0           0          0          0              0
PY-PORTAL-SHOP-HTTPS-DESARROLLO             0           0           0          0          0              0
PY-QUAD-MINDS-HTTPS       1336850   710066264     1082737  236242188    2282718              0
PY-SALDOGIROS-1            11210    12741883       30255    1945092      22858              0
PY-SALDOGIROS-2                0           0           0          0          0              0
PY-SERVICIODIGITAL-1           831      954002         833      55428       1616              0
PY-SME-COVID-1                 0           0           0          0          0              0
PY-SMT_GLOBAL-1                0           0           0          0          0              0
PY-SOUND-1                  1387     1511934         962      98691       2171              0
PY-SOUND-2                    28        6218          31       2305         44              0
PY-SOYCLARO-1                  0           0           0          0          0              0
PY-SPIRADS_SA              36314    19188023       37160    4122215      54907              0
PY-SPIRADS_SA-2            16028    20483416        9815     818757      25280              0
PY-SPIRADS_SA-3                0           0           0          0          0              0
PY-SVA_Bristol_SA-1      29594758 29406996482    21662558 3191234080   50664350              0
PY-SVA_Bristol_SA-2       1034418  1048239812      821826  227029949    1856244              0
PY-TMOBS-1                  1304      538513        1400     230364       2196              0
PY-TMOBS-3                  5779     1482514        6110    1060521       8461              0
PY-VOICENTER-1          10587898  3292026047    10344172 2100674466   20892853              0
PY-VOWIFI-VEL-1                0           0           0          0          0              0
PY-WAPPY-3                     0           0           0          0          0              0
PY-block_tunnel_fraude-2          3115     1610703       48886    5474747       8270              0
PY-block_tunnel_fraude-5             0           0           0          0          0              0
PY-block_tunnel_fraude-8             0           0           0          0          0              0
PY_MOBILESPACE_HE-1           375      482083         360      22878        717              0
WPY-AMDOCS-1                   0           0           0          0          0              0
WPY-CLARO_PORTAL-1             0           0           0          0          0              0
AUP-GM-DOMAIN1-GM-1             0           0           0          0          0              0
AUP-GM-DOMAIN1-GM-2             0           0           0          0          0              0
AUP-GM-DOMAIN2-GM-2             0           0           0          0          0              0
PY-CLARO-2                     0           0           0          0          0              0
UY-SIA-2                       0           0           0          0          0              0
PY-DIGITAL-VIRGO-1        116012    25884308      125259   19408310     180069              0
PY-DIGITAL-VIRGO-2             0           0           0          0          0              0
AUP-COTA2-1-ESIM             747      264812         656     166789       1303              0
AUP-COTA2-2-ESIM             209       43463         213     147423        405              0
AUP-COTA2-3-ESIM               0           0           0          0          0              0
AUP-NORTON-CYKADAS-HE-1           377       66501         417      65535        577              0
PY-AWG-HE-1                  105       43212         119      17771        181              0
PY-AWG-HE-2                11305     3934521       13127    2927824      19509              0
PY-AWG-HE-3                  127       34956         146      30242        200              0
PY-PORTAL_DEV_NOMINATIVIDAD-HTTP             0           0           0          0          0              0
PY-PORTAL_DEV_NOMINATIVIDAD-HTTPS             0           0           0          0          0              0
PY-PORTAL_NOMINATIVIDAD-HTTP         85394    85570373       72956    7730944     150990              0
PY-PORTAL_NOMINATIVIDAD-HTTPS        642715   133163332     1036857 1167895749    1672354              0
PY-PORTAL_TEST_NOMINATIVIDAD-HTTP             0           0           0          0          0              0
PY-PORTAL_TEST_NOMINATIVIDAD-HTTPS             0           0           0          0          0              0
AUP-GOOGLE-RCS-2        51829558 20320190783    50869179 21468165551  100565540              0
AUP-GOOGLE-RCS-3           26761    13195463       24726    4541125      48512              0
AUP-GOOGLE-RCS-4         7077690  2231815950     6991061 1922807747   13058182              0
PY-GOOGLE-RCS-6-TLSSNI        537144   310177786      467229   61093376     903681              0
AUP-DTIGNITE-3              1255      505941        1461     794245       2471              0
AUP-DTIGNITE-5                 0           0           0          0          0              0
AUP-DTIGNITE-6                 0           0           0          0          0              0
AUP-DTIGNITE-8               190       88170         211     151378        380              0
AUP-DTIGNITE-9             32806    45554378        5318     293248      38118              0
PY-CLARO-VR-HE-1               0           0           0          0          0              0
PY-CLARO-VR-HE-2               0           0           0          0          0              0

Total Ruledef(s) : 309
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ac_dict = {}
        result_dict = {}

        # initial regexp pattern
        p0 = re.compile(r'((?P<ruledef>^\S+\-\S+)\s+(?P<packets_down>\d+)\s+(?P<bytes_down>\d+)\s+(?P<packets_up>\d+)\s+(?P<bytes_up>\d+)\s+(?P<hits>\d+)\s+(?P<match>\d+))')
        p1= re.compile(r'Total Ruledef\(s\) : (?P<total_ruledef>\d+)')

        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                if 'ac_table' not in ac_dict:
                    result_dict = ac_dict.setdefault('ac_table',{})
                ruledef = m.groupdict()['ruledef']
                packets_down = m.groupdict()['packets_down']
                bytes_down = m.groupdict()['bytes_down']
                packets_up = m.groupdict()['packets_up']
                bytes_up = m.groupdict()['bytes_up']
                hits = m.groupdict()['hits']
                match = m.groupdict()['match']

                result_dict[ruledef] = {}
                result_dict[ruledef]['PACKETS_DOWN'] = packets_down
                result_dict[ruledef]['BYTES_DOWN'] = bytes_down
                result_dict[ruledef]['PACKETS_UP'] = packets_up
                result_dict[ruledef]['BYTES_UP'] = bytes_up
                result_dict[ruledef]['HITS'] = hits
                result_dict[ruledef]['MATCH'] = match
                
            
            m = p1.match(line)
            if m:
                if 'ac_table' not in ac_dict:
                    result_dict = ac_dict.setdefault('ac_table',{})
                if 'Summary' not in ac_dict['ac_table']:
                    result_dict.setdefault('Summary',{}) 
                total = m.groupdict()['total_ruledef']
                result_dict['Summary']['TOTAL'] = total
            
        return ac_dict
