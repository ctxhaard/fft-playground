let
  pkgs = import <nixpkgs> {};
in
  with pkgs;
  mkShell {
    name = "fft-playgound";
    packages = [
      (python3.withPackages (p: [p.numpy p.matplotlib]))
    ];
  }
