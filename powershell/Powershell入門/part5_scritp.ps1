# $num = 30

# if($num -gt 80){
#     Write-Host 'if root'
# }
# elseif($num -ge 50){
#     Write-Host 'elseif root'
# }
# else{
#     Write-Host 'else'
# }
# ----------------------------------------------------
# $num = 100

# switch($num){
#     {$_ -ge 80}{ Write-Host 'num > 80'}
#     {$_ -ge 50}{ Write-Host 'num >= 50'}
#     Default{ Write-Host 'Default'}
# }
# ----------------------------------------------------
# $file = 'PowerShell.zip'
# #-Regex 正規表現で一致を調べる
# #-CaseSensitive　大文字/小文字を区別して調べる

# switch -Regex -CaseSensitive ($file){
#     "\.zip$" { "$_ is zip"; break }
#     "\.ZIP$" { "$_ is ZIP"; break }
#     Default {"$_ is Unknown"}
# }


