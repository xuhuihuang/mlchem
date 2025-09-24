# Machine Learning in Chemistry (MLChem): A Data Centred, Hands-on Introductory Machine Learning Course for Undergraduate Students
This repository contains course materials for the undergraduate course: "Machine Learing in Chemistry (MLChem)", which was first offered at University of Wisconsin-Madison in Spring 2025 with the course number CHEM361 instructed by [Prof. Xuhui Huang](https://huang.chem.wisc.edu/). 

All lecture slides of MLChem, coding examples and reference notebooks have been made publicly available through the course website: [xuhuihuang.github.io/mlchem](https://xuhuihuang.github.io/mlchem/html/index.html). To maximize reproducibility and accessibility, lecture figures were generated directly from executable Jupyter notebooks, which were compiled into an online gallery using Sphinx. Each notebook functioned as a self-contained tutorial that could be viewed as a rendered webpage or executed interactively in Google Colab.

If you use materials in this repository, please cite: 

"Machine Learning in Chemistry: A Data Centred, Hands-on Introductory Machine Learning Course for Undergraduate Students", Mingyi Xue, Bojun Liu, and Xuhui Huang, ChemRxiv, DOI:

Abstract: Machine learning (ML) is rapidly reshaping the chemical sciences, with applications spanning molecular property prediction, chemical reaction design, molecular structure generation, and other data-driven discovery. With the growing integration of ML into chemical research, undergraduate chemistry students increasingly need training that bridges traditional chemical education with ML methods. Here we present Machine Learning in Chemistry (MLChem), an undergraduate-level course designed with a chemistry-first perspective to lower barriers to entry into ML while maintaining disciplinary relevance. This course introduces fundamental ML algorithms using chemical datasets, such as the small molecule solubility dataset and the peptide activity dataset. It progresses from traditional ML algorithms to neural networks, complemented by advanced modules on emerging topics such as reinforcement learning for retrosynthesis, ML-based force fields, deep learning for protein dynamics, and protein structure prediction. All source code, assignments, and lecture slides are publicly available through the course website. By combining chemical context with hands-on coding and exposure to frontier applications, MLChem equips undergraduate chemistry students with both conceptual foundations and practical skills, preparing them to participate in ML-driven chemical research.

## Visit the Course Website

The course website is now available at [xuhuihuang.github.io/mlchem](https://xuhuihuang.github.io/mlchem/html/index.html).

## How to Run A Notebook Example

Click on the `Open in Colab` badger of each gallery example.


## How to Contribute
If you want to contribute an example notebook, add your example to `notebooks/`. When there's a new subdirectory created, please add the `toc` to `docs/examples.rst`.

If you want to contribute lecture slides, add your pdf file to `lectures/`. After that, manually add the item to `docs/lectures.rst`:
```markdown
- `Chapter XX: Title <_static/lectures/newly_added.pdf>`_
```

If you want to contribute homeworks, add your homework folder (including the problem set, answer key and reference notebooks) to `homeworks/`. After that, manually add the item to `docs/homeworks.rst`:
```markdown
#. HW XX: Title

   - `HWX Problem Set <_static/homeworks/hwXX/problem_set.pdf>`_
   - `HWX Reference Notebooks <homeworks/hwXX/notebook.html>`_
```


## How to Build Document

See [Build Doc README](./docs/README.md).








