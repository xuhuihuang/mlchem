# Machine Learning in Chemistry (MLChem): A Data Centred, Hands-on Introductory Machine Learning Course for Undergraduate Students

This repository contains example Jupyter notebook tutorials for applying ML methods to chemical datasets. These tutorials are associated with the undergraduate course: "Machine Learing in Chemistry (MLChem)", which was first offered at University of Wisconsin-Madison in Spring 2025 with the course number CHEM361 instructed by [Prof. Xuhui Huang](https://huang.chem.wisc.edu/). In this course, results from applying ML methods to chemical datasets were generated directly from executable Jupyter notebooks used in the lecture slides. These notebooks have been compiled into an online gallery with Sphinx. Each notebook is a self-contained tutorial that can be viewed as a rendered webpage or run interactively in Google Colab. The corresponding lecture slides are also embedded within each notebook.

If you use materials in this repository, please cite: 

["Machine Learning in Chemistry: A Data Centred, Hands-on Introductory Machine Learning Course for Undergraduate Students"](https://chemrxiv.org/engage/chemrxiv/article-details/68e029acdfd0d042d1e0312e), Mingyi Xue, Bojun Liu, and Xuhui Huang, ChemRxiv, DOI: [10.26434/chemrxiv-2025-9zldf](https://chemrxiv.org/engage/chemrxiv/article-details/68e029acdfd0d042d1e0312e)

## Visit the Course Website

The course website is now available at [xuhuihuang.github.io/mlchem](https://xuhuihuang.github.io/mlchem/html/index.html).

## How to Run A Notebook Example

Click on the `Open in Colab` badger of each gallery example.


## How to Contribute your own Jupyter notebook tutorials for MLChem 
If you want to contribute an example notebook to an existing category, add the example notebook to `examples/<subfolder>/`. After that manually add the item to the corresponding chapter `docs/examples.rst` to make it show up on the course website.


<!-- If you want to contribute lecture slides, add your pdf file to `lectures/`. After that, manually add the item to `docs/lectures.rst`:
```markdown
- `Chapter XX: Title <_static/lectures/newly_added.pdf>`_
``` -->

If you want to contribute homeworks, add your homework folder (including the problem set, answer key and reference notebooks) to `homeworks/`. After that, manually add the item to `docs/homeworks.rst`:
```markdown
#. HW XX: Title

   - `HWX Problem Set <_static/homeworks/hwXX/problem_set.pdf>`_
   - `HWX Reference Notebooks <homeworks/hwXX/notebook.html>`_
```


## How to Build Document

See [Build Doc README](./docs/README.md).

