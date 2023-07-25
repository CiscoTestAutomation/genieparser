expected_output ={
    'certificates': {
        1: 'MIIDQzCCAiugAwIBAgIQX/h7KCtU3I1CoxW1aMmt/zANBgkqhkiG9w0BAQUFADA1MRYwFAYDVQQKEw1DaXNjbyBTeXN0ZW1zMRswGQYDVQQDExJDaXNjbyBSb290IENBIDIwNDgwHhcNMDQwNTE0MjAxNzEyWhcNMjkwNTE0MjAyNTQyWjA1MRYwFAYDVQQKEw1DaXNjbyBTeXN0ZW1zMRswGQYDVQQDExJDaXNjbyBSb290IENBIDIwNDgwggEgMA0GCSqGSIb3DQEBAQUAA4IBDQAwggEIAoIBAQCwmrmrp68Kd6ficba0ZmKUeIhHxmJVhEAyv8CrLqUccda8bnuoqrpu0hWISEWdovyD0My5jOAmaHBKeN8hF570YQXJFcjPFto1YYmUQ6iEqDGYeJu5Tm8sUxJszR2tKyS7McQr/4NEb7Y9JHcJ6r8qqB9qVvYgDxFUl4F1pyXOWWqCZe+36ufijXWLbvLdT6ZeYpzPEApk0E5tzivMW/VgpSdHjWn0f84bcN5wGyDWbs2mAag8EtKpP6BrXruOIIt6keO1aO6g58QBdKhTCytKmg9lEg6CTY5j/e/rmxrbU6YTYK/CfdfHbBcl1HP7R2RQgYCUTOG/rksc35LtLgXfAgEDo1EwTzALBgNVHQ8EBAMCAYYwDwYDVR0TAQH/BAUwAwEB/zAdBgNVHQ4EFgQUJ/PIFR5umgIJFq0roIlgX9p7L6owEAYJKwYBBAGCNxUBBAMCAQAwDQYJKoZIhvcNAQEFBQADggEBAJ2dhISjQal8dwy3U8pORFBi71R803UXHOjgxkhLtv5MOhmBVrBW7hmWYqpao2TB9k5UM8Z3/sUcuuVdJcr18JOagxEu5sv4dEX+5wW4q+ffy0vhN4TauYuXcB7w4ovXsNgOnbFp1iqRe6lJT37mjpXYgyc81WhJDtSd9i7rp77rMKSsH0T8laszBvt9YAretIpjsJyp8qS5UwGH0GikJ3+r/+n6yUA4iGe0OcaEb1fJU9u6ju7AQ7L4CYNu/2bPPu8Xs1gYJQk0XuPL1hS27PKSb3TkL4Eq1ZKR4OCXPDJoBYVL0fdX4lIdkxpUnwVwwEpxYB5DC2Ae/qPOgRnhCzU=',
        2: 'MIIEPDCCAySgAwIBAgIKYQlufQAAAAAADDANBgkqhkiG9w0BAQUFADA1MRYwFAYDVQQKEw1DaXNjbyBTeXN0ZW1zMRswGQYDVQQDExJDaXNjbyBSb290IENBIDIwNDgwHhcNMTEwNjMwMTc1NjU3WhcNMjkwNTE0MjAyNTQyWjAnMQ4wDAYDVQQKEwVDaXNjbzEVMBMGA1UEAxMMQUNUMiBTVURJIENBMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0m5l3THIxA9tN/hS5qR/6UZRpdd+9aE2JbFkNjht6gfHKd477AkS5XAtUs5oxDYVt/zEbslZq3+LR6qrqKKQVu6JYvH05UYLBqCj38s76NLk53905Wzp9pRcmRCPuX+a6tHF/qRuOiJ44mdeDYZo3qPCpxzprWJDPclM4iYKHumMQMqmgmg+xghHIooWS80BOcdiynEbeP5rZ7qRuewKMpl1TiI3WdBNjZjnpfjg66F+P4SaDkGbBXdGj13oVeF+EyFWLrFjj97fL2+8oauV43Qrvnf3d/GfqXj7ew+z/sXlXtEOjSXJURsyMEj53Rdd9tJwHky8neapszS+r+kdVQIDAQABo4IBWjCCAVYwCwYDVR0PBAQDAgHGMB0GA1UdDgQWBBRI2PHxwnDVW7t8cwmTr7i4MAP4fzAfBgNVHSMEGDAWgBQn88gVHm6aAgkWrSugiWBf2nsvqjBDBgNVHR8EPDA6MDigNqA0hjJodHRwOi8vd3d3LmNpc2NvLmNvbS9zZWN1cml0eS9wa2kvY3JsL2NyY2EyMDQ4LmNybDBQBggrBgEFBQcBAQREMEIwQAYIKwYBBQUHMAKGNGh0dHA6Ly93d3cuY2lzY28uY29tL3NlY3VyaXR5L3BraS9jZXJ0cy9jcmNhMjA0OC5jZXIwXAYDVR0gBFUwUzBRBgorBgEEAQkVAQwAMEMwQQYIKwYBBQUHAgEWNWh0dHA6Ly93d3cuY2lzY28uY29tL3NlY3VyaXR5L3BraS9wb2xpY2llcy9pbmRleC5odG1sMBIGA1UdEwEB/wQIMAYBAf8CAQAwDQYJKoZIhvcNAQEFBQADggEBAGh1qclr9tx4hzWgDERm371yeuEmqcIfi9b9+GbMSJbiZHc/CcCl0lJu0a9zTXA9w47H9/t6leduGxb4WeLxcwCiUgvFtCa51Iklt8nNbcKY/4dw1ex+7amATUQO4QggIE67wVIPu6bgAE3Ja/nRS3xKYSnj8H5TehimBSv6TECii5jUhOWryAK4dVo8hCjkjEkzu3ufBTJapnv89g9OE+H3VKM4L+/KdkUO+52djFKnhyl47d7cZR4DY4LIuFM2P1As8YyjzoNpK/urSRI14WdIlplR1nH7KNDl5618yfVP0IFJZBGrooCRBjOSwFv8cpWCbmWdPaCQT2nwIjTfY8c=',
        3: 'MIIDgTCCAmmgAwIBAgIEAmhA5TANBgkqhkiG9w0BAQsFADAnMQ4wDAYDVQQKEwVDaXNjbzEVMBMGA1UEAxMMQUNUMiBTVURJIENBMB4XDTE4MDMyNzE4NTUzNFoXDTI5MDUxNDIwMjU0MVowbTEpMCcGA1UEBRMgUElEOkM5NDAwLVNVUC0xWEwgU046SkFFMjIxMjA5WlMxDjAMBgNVBAoTBUNpc2NvMRgwFgYDVQQLEw9BQ1QtMiBMaXRlIFNVREkxFjAUBgNVBAMTDUM5NDAwLVNVUC0xWEwwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC4pTwS3+awvyYU0PhxbomDplGlfset4yioGIridLJb+auZc2GeGubvG/aKd3yLHZJXFfS20BfnsO9IJyFjpi9Kc0oDebx9xYnk+1O6cTGo7DVblUnplhUG/A9D80EpZ6VwJ3TNzVv5cpBRNDHyFcSqmw+N403b2WyJbCAVnlgQZG71KTrsVeH1M982mEXrrm01DaXtrmj+WJVpVZGqsVw3g7nc7cxCfQYydeFAidRPViw3RAxpVF/MxROc/EDqkSzvBJpa0Noo7Q8Gg8g86DoJW3+uLWAXEcRDiQNV0W3aQ8HMm2UipXDr7ZCUQrgA2bBUw7Dg8AF+JZPSQWpTwnm1AgMBAAGjbzBtMA4GA1UdDwEB/wQEAwIF4DAMBgNVHRMBAf8EAjAAME0GA1UdEQRGMESgQgYJKwYBBAEJFQIDoDUTM0NoaXBJRD1VWUpRT0VnNUZ3RllWMlZrSUZObGNDQWdOaUF4TXpvME9Ub3hNU0RpditVPTANBgkqhkiG9w0BAQsFAAOCAQEAVZ3s8Hx+mCL0DN7MhJbUTaX6YjMvKEmC9JyxGPHvpviRIg4TCnILU3UlAcr3aSxC0/Z7ApO3axjtKVkQTKO2kCEmGbeUFDusbzE3KK6Zuw3uUS/0JeiUvgN8w+/8hQ0kUS1fjtWO03K4547huC10k7t1uHZwkSIr9cCinQw7wUGWc2BHJeOrl7+TtDIOp5tTYysII8O5T1CXO22m0I7laQ2FGVdb/ngAd0BRatUlOsklowM0PFuVmIGRG/IWIWg8BvYfS9jm8XBn4bzNA8HQcsM20txZaH02AxzeEOz+YoikRWjA3+JUUcY0pMutr6SVxRbe6CoJ8GTJk7eIXted8w=='
        },
       'signature_version': 1,
       'signature': 'A59DA741EA66C2AFC006E1766B3B11493A79E67408388C40160C2729F88281E945AA95C23837350E2F3A082A9D359B27CDD6A20717C7485FF43F34DC2DC98C8304DABC51F11AFF7417469E2BAA15BAB069B7C6B40C7E80F31A4AA2D137286FB61D5CE4CF4D638EF68BE81BEE982A3BBD017BAE067D9ABF42237FF2C973AD392D61F05E3B77301B45C07FF13994ADF648C076B303EB280DD5059F9B82EC20692C5BF21ECE589865205EB6695DA000CAE20DFC6A6BD83E081D8DC6134C315E6E5F8A8B80AEF2916221F6977EF7B2ACB871E4A42AF2B4780672267615DB0C98196775FD2A3A3186AE10CC837D3BC555A50BB1323F1EDF5AAD92FBA4CAA240A8EC99'
    }