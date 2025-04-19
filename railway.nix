{ pkgs }:
pkgs.mkShell {
  buildInputs = [
    pkgs.ffmpeg
    pkgs.python311
    pkgs.python311Packages.fastapi
    pkgs.python311Packages.uvicorn
    pkgs.python311Packages.pillow
    pkgs.python311Packages.pydub
  ];
}
