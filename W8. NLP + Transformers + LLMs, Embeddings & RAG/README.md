## SHOPSMART BUILD — Milestone 5 complete ##
ShopSmart reads its own reviews at scale, routes complaints by theme, and answers support questions grounded in real policy. Notice the reuse: KNN became vector search, K-Means became theme discovery, Week 4 metrics graded the sentiment model.

## 1.	Prompt Engineering: 
It uses a pre-trained language model and carefully designed prompts to improve responses. It has very low implementation cost, no model training required and is quick to deploy but cannot access shop smarts private FAQ or company documents unless they are included in every prompt and may generate incorrect or outdated information.
## 2.	RAG
It stands for “retrieval augmented generation”. it retrieves relevant information from shop smarts FAQ documents before generating and answer. It provides answers based on company documents, is easy to update by modifying the FAQ database without retraining the model and reduces hallucinations by grounding response in retrieved information but requires and embedding model and a retrieved system as well as retrieved quality depends on document quality and similarity search.
## 3.	 Fine Tuning
It retrains a pre-trained language model using company specific data. It produces responses in consistent style and learns specialized terminology and domain specific language but has high training cost, requires large labelled datasets and updating information requires retraining the model.
## Best option for ShopSmart
On basis of cost, prompt engineering has lowest cost, RAG has moderate and fine tuning as highest cost. Prompt engineering includes risk of inaccurate or hallucinated answers when a company specific information is missing, RAG has risk of retrieving irrelevant documents if embedding or retrieval are poor and fine tuning has risk of out-dated knowledge if business policies change after training as they require training.
For shop smarts support assistant RAG is recommended as data changes overtime such as policies etc such that RAG allows the data to be updated without retraining the model and still providing the accurate information

