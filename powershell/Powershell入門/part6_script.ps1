#値が二倍にされていく

# $array = 1..3

# for ($x = 0; $x -lt $array.Count; $x++){
#     Write-Host ($array[$x] * 2)
# }
# ------------------------------------------------

#値が二乗されていく
# $collection = 1..3

# foreach ($item in $collection ){
#     Write-Host([Math]::Pow($item,2))
# }
# ------------------------------------------------

# #while文quitが入力されるまで繰り返す。
# $command = ""
# while ($command -notmatch "quit"){
#     $command = Read-Host "Enter your Command"
# }
# ------------------------------------------------

#while do の使い方
# $command = ""
# do{
#     $command = Read-Host "Please quit"
# } while ($command -ne "quit")
# ------------------------------------------------
# while doとwhileの違い
# while文は先の処理が行われ変数の値を入力し終わる
# while-do文は変数を認識しない

# $command = "quit"

# # while ($command -notmatch "quit"){
# #     $command = Read-Host "Enter your Command"
# # }

# do{
#     $command = Read-Host "Please quit"
# } while ($command -ne "quit")
# ------------------------------------------------
# $array = 1..3
# $limit = $array[-1] # 配列の一番最後の要素。今回の場合は3
# :outer foreach ($y in $array){
#     foreach ($x in $array){
#         if($x -eq $limit){
#             Write-Host "limit break"
#             break outer
#         }
#         Write-Host $x $y
#     }
# }