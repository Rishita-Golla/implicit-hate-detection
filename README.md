# implicit-hate-detection
cs685 group project implicit hate detection

Wandb Team: https://wandb.ai/umass-iesl-is/685-cs-project || https://wandb.ai/umass-iesl-is/cs685-project/


Proposal: (link-to-proposal)

Group members: Simon Andrews, Kimberley Faria, Rishita Golla, Pragya Sarda

Task List: https://github.com/users/kimberley-faria/projects/1/views/1 

Key Reference Paper: https://aclanthology.org/2021.emnlp-main.29.pdf (Presents the Implicit Hate Dataset)

TODO: (Write short descriptions of (interesting) papers, will be easier to recall as we go through the project)

Imtermediate Fine-tuning:

**Mohit's lec on Intermediate finetuning: https://www.youtube.com/watch?v=run0nnEBVFU&ab_channel=MohitIyyer**

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



# Proposal Feedback:
Very interesting and thoughtful proposal. It is also great that the dataset and evaluation bench mark are available. A few minor comments from us:

1. One thing that could be informative and interesting is that you may want to compute and show your existing evaluation metrics (F1, accuracy …) also based on various classes. That may be very interesting for your error analysis too.

2. Depending on the error analysis you made on step 1, you may discover that there might be areas where the model is bad. Then you could potentially fine-tune BERT for that types of dataset before fine-tuning it for the hate speech detection task. For example, maybe it could be helpful to fine-tune BERT on sarcasm / humor detection tasks.

3. BERT has never seen twitter text during pre-training so there might be domain adaptation issues. It might also be interesting to see whether BERT will do better on your hate speech detection task (twitter text) after being fine-tuned on twitter text first.


Good luck,
Shufan


# Questions for OH:

1. task definition in the paper doesn't match the dataset, can we specify how we are running our baselines in the report and move forward? - **doesn't match, so can establish 2 baselines - implicit-hate vs non-hate (drop the 1000 explicit hate) and hate vs non-hate (combine the 2 categories). Need to check overlap between stage 1 and stage 2 annotations**
2. Should we spend time on SVM baselines? might be better to focus on the BERT baselines and what is asked in the proposal. - **yup, can just concentrate on BERT**
3. Analysis and finetuning approach -> how should we prioritize our experiments?

    1. **for twitter data issue - analyze examples for mistakes - will mostly be the ones with certain linguistic details in social media text (acronyms, hashtags, etc)** 
    2. **for the 6-way classification task => directions for negative flips -> identify pairs , compute the confusion matrix (# of examples from 1 class to another, which are overlapping), which label pair gets wrongly classified the most**
    3. **for which class does the model make the most mistakes**
    
4. finetuning approach on twitter text data?  simple LM objective? (there should be a twitter BERT already out there) - https://huggingface.co/docs/transformers/model_doc/bertweet - **yes can use this pre-trained BERT**
5. evaluate on all hparam settings? or just the best model
6. not writing model from scratch - is what we are doing sufficient.

