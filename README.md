# implicit-hate-detection
cs685 group project implicit hate detection

Proposal: (link-to-proposal)

Group members: Simon Andrews, Kimberley Faria, Rishita Golla, Pragya Sarda

Key Reference Paper: https://aclanthology.org/2021.emnlp-main.29.pdf (Presents the Implicit Hate Dataset)

TODO: (Write short descriptions of (interesting) papers, will be easier to recall as we go through the project)

Imtermediate Fine-tuning:
Key Paper: https://arxiv.org/pdf/1811.01088.pdf (Presents the concept of STILTS and Intermediate Fine-tuning)

Other Papers (How to choose tasks, analysis of intermediate fine-tuning, what works, might help in selecting the intermediate tasks and running experiments):
- https://arxiv.org/abs/2005.00628 - Intermediate-Task Transfer Learning with Pretrained Models for Natural Language Understanding: When and Why Does It Work?
- https://arxiv.org/abs/2108.11696 - Rethinking Why Intermediate-Task Fine-Tuning Works
- https://arxiv.org/abs/2104.08247v2 - What to Pre-Train on? Efficient Intermediate Task Selection

Some other interesting related works:
- https://arxiv.org/abs/2005.02439 - Contextualizing Hate Speech Classifiers with Post-hoc Explanation (this paper has another dataset - the GAB Corpus, which contains implicit hate data, they also present " extract SOC post-hoc explanations from fine-tuned BERT classifiers to efficiently detect bias towards identity terms.", this might be of interest to us)
- https://arxiv.org/pdf/1710.07394.pdf - Recognizing Explicit and Implicit Hate Speech Using a Weakly Supervised Two-path Bootstrapping Approach
- https://arxiv.org/pdf/1703.04009.pdf - Automated Hate Speech Detection and the Problem of Offensive Language

Possible intermediate tasks (datasets):

1.  SemEval 2015 task on the sentiment analysis of figurative language on Twitter (Task 11). - 
    - This is the first sentiment analysis task wholly dedicated to analyzing figurative language on Twitter. Specifically, three broad classes of figurative language are considered: irony, sarcasm and metaphor. 
    - https://alt.qcri.org/semeval2015/task11/ 
    - https://aclanthology.org/S15-2080.pdf
    
2.  SemEval 2021 task on Toxic Spans Detection
    - The Toxic Spans Detection task concerns the evaluation of systems that detect the spans that make a text toxic, when detecting such spans is possible.
    - https://sites.google.com/view/toxicspans
    - https://aclanthology.org/2021.semeval-1.6.pdf
3.  HSOL (Hate speech and offensive language) - https://github.com/t-davidson/hate-speech-and-offensive-language
4.  Gab Hate Corpus
    - https://osf.io/edua3/ 
5.  Language Modelling - Sarcastic Text Generation - https://arxiv.org/abs/1911.10401 (A Transformer-based approach to Irony and Sarcasm detection)


