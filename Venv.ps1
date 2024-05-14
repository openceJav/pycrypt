# Running this script will activate the virtual environment if it exists in '.venv'.
$venvPath = '.\.venv\Scripts\Activate.ps1'

if (Test-Path $venvPath) {
    Write-Host "Script Run: Virtual Environment Found, Virtual Environment Activated."
    . $venvPath

} else {
    Write-Host "Run: Virtual Environment Not Found."
    
}