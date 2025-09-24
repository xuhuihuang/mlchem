# Build Documentation for Chem361

## OS Dependency
It is recommended to use GitHub Actions or a Linux environment to compile this document.

## Compiling Environment
```bash
conda create -n chem361-doc python=3.10
conda activate chem361-doc

sudo apt-get install -y pandoc
pip install -r requirements.txt
```

## Compile
```bash
# build html
# under docs/
make html
```

## Clean up
```bash
# under docs/
make clean
```

##  Deploy

The website is available at [xuhuihuang.github.io/mlchem](https://xuhuihuang.github.io/mlchem/html/index.html).
