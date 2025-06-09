expected_output = {
    "vrf":{
      "default":{
         "address_family":{
            "ipv6":{
               "routes":{
                  "fc00:a000:1000::2/128":{
                     "route":"fc00:a000:1000::2/128",
                     "ip":"fc00:a000:1000::2",
                     "mask":"128",
                     "active":True,
                     "known_via":"isis SRv6_Region",
                     "metric":10,
                     "distance":115,
                     "type":"level-2",
                     "installed":{
                        "date":"Jun 11 10:43:11.718",
                        "for":"1d18h"
                     }
                  }
               }
            }
         }
      }
   }
}