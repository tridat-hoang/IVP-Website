[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$files = Get-ChildItem "c:\Users\Admin\Claude\Projects\IVP Website" -Filter "*IVP_1 (5).docx"
$docPath = $files[0].FullName
Write-Host "Opening: $docPath"
$doc = $word.Documents.Open($docPath)
$text = $doc.Content.Text
$doc.Close($false)
$word.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
$text | Out-File -FilePath "c:\Users\Admin\Claude\Projects\IVP Website\docs\content_v5.txt" -Encoding UTF8
Write-Host "Done - extracted text"
