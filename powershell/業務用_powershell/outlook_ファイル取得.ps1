$o = New-Object -comobject outlook.application
$n = $o.GetNamespace("MAPI")
$filepath = "ローカルファイルパス"
$f = $n.PickFolder()
$f.Items| foreach {
  $_.attachments|foreach {
    $_.saveasfile((Join-Path $filepath $_.filename))
  }
}