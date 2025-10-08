.. .. image:: _static/figs/logo.png
..    :alt: ML Chem Logo
..    :align: center
..    :width: 300px

Jupyter Notebook Tutorials for Machine Learning in Chemistry (MLChem) 
==============================================================================================================================

This website hosts the Jupyter Notebook gallery for the undergraduate course Machine Learning in Chemistry (MLChem), first offered at the University of Wisconsin–Madison in Spring 2025 as CHEM 361, taught by `Prof. Xuhui Huang <https://huang.chem.wisc.edu/>`_. In this course, results from applying ML methods to chemical datasets were generated directly from executable Jupyter notebooks used in the lecture slides. These notebooks have been compiled into an online gallery with Sphinx. Each notebook is a self-contained tutorial that can be viewed as a rendered webpage or run interactively in Google Colab. The corresponding lecture slides are also embedded within each notebook.



.. toctree::
   :maxdepth: 1
   :caption: Contents:

   Home <self>
   examples.rst
   homeworks.rst
   how2cite.rst



Course Syllabus
---------------

.. list-table::
   :header-rows: 1
   :widths: 15 40 30 15

   * - Chapter
     - Contents
     - `Tutorial Notebooks <examples.rst>`_
     - `Assignments <homeworks.rst>`_
   * - Chapter 1
     - Introduction and Setup of the Coding Environment
     - 🎓 EnvSetup_
     - 💼 HW0_
   * - Chapter 2
     - From Molecules to Features – Preparing Training Data
     - 💻 Descriptors_, 💻 Fingerprints_
     - 💼 HW1_
   * - Chapter 3
     - Uncovering Patterns in Chemistry – Unsupervised Learning and Dimensionality Reduction
     - 💻 KMeans_, 💻 KCenter_, 💻 DBSCAN_, 💻 AgglomerativeClustering_, 💻 PCA_
     - 
   * - Chapter 4
     - Predicting Chemical Outcomes – Supervised Learning for Classification and Regression
     - 💻 LinReg_, 💻 OverfitCV_, 💻 Regularization_, 💻 LogReg_, 💻 kNN_, 💻 DecisionTree_
     - 💼 HW2_
   * - Chapter 5
     - Neural Networks – Fundamentals and Applications in Chemical Modeling
     - 💻 XOR_, 💻 Softmax_, 💻 MLP_, 💻 OverfitNN_
     - 
   * - Chapter 6
     - Deep Neural Networks – Advanced Architectures for Chemical Applications
     - 💻 CNN_, 💻 GNN_, 💻 RNN_
     - 💼 HW3_
   * - Chapter 7
     - Generating Chemical Data – AI Generative Models
     - 💻 VAE_
     - 
   * - Chapter 8
     - Transforming Chemistry with Large Language Models – From Chemical to Protein Language Models
     - 💻 ESM2_
     - 💼 HW4_
   * - Chapter 9
     - Machine Learning Force Fields – New Energy Functions in Chemical Simulations
     - 
     - 
   * - Chapter 10
     - Reinforcement Learning for Chemical Discovery – Enabling Automated Synthesis
     - 
     - 
   * - Chapter 11
     - Understanding Dynamics – ML Models for Molecular Simulations
     - 
     - 
   * - Chapter 12
     - Predicting Protein Structure – AlphaFold and Its Applications
     - 
     - 

.. _EnvSetup: _static/lectures/Tutorial_Python_Environment_Setup.pdf
.. _Descriptors: examples/representation/Reference_Ch2_molecular_properties.html
.. _Fingerprints: examples/representation/Reference_Ch2_fingerprints.html
.. _KMeans: examples/cluster/Reference_Ch3_part_1_kmeans_from_scratch.html
.. _KCenter: examples/cluster/Reference_Ch3_part_1_kcenter_from_scratch.html
.. _DBSCAN: examples/cluster/Reference_Ch3_part_1_dbscan_from_scratch.html
.. _AgglomerativeClustering: examples/cluster/Reference_Ch3_part_1_agglomerative_from_scratch.html
.. _PCA: examples/reduction/Reference_Ch3_part_1_pca_step_by_step.html
.. _LinReg: examples/linear_models/Reference_Ch4_Part_1_linear_regression.html
.. _OverfitCV: examples/linear_models/Reference_Ch4_Part_1_polynomial_fitting_overfitting_and_cross_validation.html
.. _Regularization: examples/linear_models/Reference_Ch4_Part_1_regularization_effect_explained.html
.. _LogReg: examples/linear_models/Reference_Ch4_Part_1_logistic_regression.html
.. _kNN: examples/non_parametric/Reference_Ch4_part_2_kNN.html
.. _DecisionTree: examples/non_parametric/Reference_Ch4_part_2_decision_tree.html
.. _XOR: examples/nn/Reference_ch5_Part_2_xor.html
.. _Softmax: examples/nn/Reference_Ch5_Part_1_multi_class_softmax_regression.html
.. _MLP: examples/nn/Reference_Ch5_Part_3_MLP.html
.. _OverfitNN: examples/nn/Reference_Ch5_Part_4_avoid_overfitting_techniques.html
.. _CNN: examples/deep_nn/Reference_ch6_Part_1_CNNs_colab.html
.. _GNN: examples/deep_nn/Reference_ch6_Part_2_GNN_colab.html
.. _RNN: examples/deep_nn/Reference_ch6_Part_3_rnn_colab.html
.. _VAE: examples/generative/Reference_Ch7_VAE_colab.html
.. _ESM2: examples/transformer/Reference_Ch8_PLM_colab.html
.. _HW0: _static/homeworks/hw0/Chem361_hw0.pdf
.. _HW1: _static/homeworks/hw1/Chem361_hw1.pdf
.. _HW2: _static/homeworks/hw2/Chem361_hw2.pdf
.. _HW3: _static/homeworks/hw3/Chem361_hw3.pdf
.. _HW4: _static/homeworks/hw4/Chem361_hw4.pdf



How to contribute
------------------
To maximize reproducibility and accessibility, we maintain the source code and notebooks at this repository `xuhuihuang/mlchem <https://github.com/xuhuihuang/mlchem>`_. If you would like to contribute, please feel free to open an issue or a pull request to this repository.


How to cite
-----------

If you use materials in this repository, please cite:

"Machine Learning in Chemistry: A Data Centred, Hands-on Introductory Machine Learning Course for Undergraduate Students", Mingyi Xue, Bojun Liu, and Xuhui Huang, ChemRxiv, DOI: `10.26434/chemrxiv-2025-9zldf
 <https://chemrxiv.org/engage/chemrxiv/article-details/68e029acdfd0d042d1e0312e>`_ 







