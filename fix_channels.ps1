$path2 = "Website-Clone-2/assets/data/india-channels.json"
$path1_etv = "Website-Clone/assets/data/etv-channels.json"

$data2 = Get-Content -Raw $path2 | ConvertFrom-Json
$etv_data = Get-Content -Raw $path1_etv | ConvertFrom-Json

$hash2 = @{}
foreach ($prop in $data2.PSObject.Properties) {
    if ($prop.Value.name -notlike "*ETV Telugu HD*") {
        $hash2[$prop.Name] = $prop.Value
    } else {
        Write-Host "Removing $($prop.Name)"
    }
}

foreach ($prop in $etv_data.PSObject.Properties) {
    $hash2[$prop.Name] = $prop.Value
    Write-Host "Adding $($prop.Name)"
}

$json = $hash2 | ConvertTo-Json -Depth 10 -Compress
Set-Content -Path $path2 -Value $json
