# Multi-Agent RAG Prototype Using LangGraph

This repository contains a **prototype Retrieval-Augmented Generation (RAG) system** built to experiment with **LangGraph-based multi-agent workflows** over enterprise documents.

The goal of this project is to validate:
- Agent orchestration patterns
- State-driven workflows
- Retrieval-based answering correctness

FAISS and local embeddings are used **only for prototyping and testing** and are not assumed to be long-term infrastructure choices.

---

## Purpose of This Project

This project exists to:
- Explore LangGraph as an agent workflow orchestrator
- Test multi-agent separation of responsibilities
- Validate RAG behavior on structured enterprise-style documents
- Serve as a foundation for later replacement of retrieval and model components

This is not intended to be a finalized production system.

---

## Architecture Overview

The system is composed of three explicit agents orchestrated using LangGraph:

1. Query Analyzer  
   Interprets the user question and prepares a retrieval query.

2. Retriever  
   Retrieves relevant document chunks from a vector index.

3. Answer Generator  
   Produces an answer strictly using retrieved context.

The workflow is linear and deterministic to simplify debugging and evaluation.

---

## Project Structure

