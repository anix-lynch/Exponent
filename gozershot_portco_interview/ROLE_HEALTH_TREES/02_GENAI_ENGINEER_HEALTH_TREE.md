# GENAI ENGINEERING HEALTH TREE
## (Hallucinations Cost Money)

```
                                      [GENAI]
                                         |
                                         |
        -------------------------------------------------------------------------
        |                          |                          |                 |
        |                          |                          |                 |
   [1] HALLUCINATION          [2] RETRIEVAL QUALITY     [3] CONTEXT WINDOW    [4] COST PER QUERY
   AI พูดโกหก                 หาข้อมูลผิด               ใส่ข้อมูลมากเกิน      ใช้เงินมากเกิน
   เพราะไม่มี grounding      เพราะ vector search พัง    เพราะ token limit     เพราะ API ราคาแพง

        |                          |                          |                 |
        |                          |                          |                 |

   Hallucination Rate        Retrieval Precision        Context Overflow      Cost per 1K Tokens
   (facts vs generated)     (relevant docs found)      (input > model limit)  (API pricing)

        |                          |                          |                 |
        |                          |                          |                 |

   < 5%       GROUNDED       > 80%    EXCELLENT        < 80%    SAFE          < $0.01   CHEAP
   5–15%      WARNING        60–80%    GOOD             80–95%   RISKY         $0.01–0.05 ACCEPTABLE
   > 15%      LYING          < 60%    BROKEN            > 95%    OVERFLOW      > $0.05   EXPENSIVE

        |                          |                          |                 |
        |                          |                          |                 |

   Impact:                   Impact:                    Impact:             Impact:
   Wrong answers             Irrelevant context         Truncated responses  Budget overrun
   User loses trust          Model confused             Lost information     Project cancelled
   Legal issues              Bad recommendations         Poor quality         Cost kills ROI

        |                          |                          |                 |
        -------------------------------------------------------------------------
                                         |
                                         |
                               GENAI RELIABILITY SCORE

                         If ANY pillar is RED:
                         → AI gives wrong answers
                         → Users lose trust
                         → Project gets cancelled
```

---

## 🎯 INTENT BEHIND GENAI ENGINEER QUESTIONS

### [1] HALLUCINATION - "Why does RAG grounding matter?"

**Intent**: Test if you understand the fundamental GenAI problem

**What they're really testing:**
- Do you know LLMs hallucinate?
- Can you ground responses in real data?
- Do you understand RAG architecture?

**Questions map to:**
- "How do you implement RAG in your BI agent?" → Tests grounding
- "How do you ensure retrieved documents are relevant?" → Tests quality
- "What happens when query returns no relevant documents?" → Tests edge cases

**Why it matters:**
- AI says "Revenue is $5M" → Actually $3M → Wrong business decisions
- AI makes up facts → Legal issues
- Users lose trust → Product fails

**Your portfolio shows:**
- Mocktailverse: "How do you measure the quality of retrieved documents?"
- AI BI Agent: "How do you implement RAG in your BI agent?"
- This is THE core GenAI skill

---

### [2] RETRIEVAL QUALITY - "Why does vector search matter?"

**Intent**: Test if you understand semantic search

**What they're really testing:**
- Do you know how to find relevant documents?
- Can you optimize vector search?
- Do you understand embedding quality?

**Questions map to:**
- "How did you optimize vector search performance?" → Tests optimization
- "What's your reranking strategy?" → Tests quality improvement
- "How do you implement semantic job matching?" → Tests vector search

**Why it matters:**
- Bad retrieval = wrong context = wrong answers
- User asks "tropical drinks" → Gets "winter cocktails" → Bad experience
- Model confused by irrelevant context

**Your portfolio shows:**
- Mocktailverse: "How did you optimize vector search performance?"
- AI Agent Job Intelligence: "How do you implement semantic job matching?"
- This is core to RAG systems

---

### [3] CONTEXT WINDOW - "Why does chunking matter?"

**Intent**: Test if you understand token limits

**What they're really testing:**
- Do you know model context limits?
- Can you chunk documents properly?
- Do you understand token management?

**Questions map to:**
- "How did you decide on chunk size?" → Tests chunking strategy
- "How do you manage context window limits?" → Tests token management
- "How do you handle documents too large for single chunk?" → Tests edge cases

**Why it matters:**
- Input > model limit → Truncation → Lost information
- Bad chunking → Context broken → Wrong answers
- Too many chunks → Cost explosion

**Your portfolio shows:**
- Mocktailverse: "How did you decide on chunk size for document processing?"
- Mocktailverse: "How do you manage context window limits when retrieving documents?"

---

### [4] COST PER QUERY - "Why does cost optimization matter?"

**Intent**: Test if you understand GenAI economics

**What they're really testing:**
- Do you know API costs?
- Can you optimize for cost?
- Do you understand cost vs quality trade-offs?

**Questions map to:**
- "How did you handle costs for embedding generation at scale?" → Tests cost awareness
- "How do you optimize Bedrock API calls?" → Tests optimization
- "What's your approach to managing API costs?" → Tests cost management

**Why it matters:**
- $0.05 per query × 1M queries = $50K/month
- Cost kills project ROI
- Budget overrun → Project cancelled

**Your portfolio shows:**
- Mocktailverse: "How did you handle costs for embedding generation at scale?"
- Mocktailverse: "You mention the system costs $1-2/month. How did you achieve that?"
- This shows production thinking

---

## 🔥 FAILURE MODES

### If HALLUCINATION > 15%:
- AI gives wrong answers
- Users lose trust
- Legal/compliance issues
- **You get fired when AI lies to customers**

### If RETRIEVAL QUALITY < 60%:
- Wrong context retrieved
- Model confused
- Bad recommendations
- **You get fired when users complain**

### If CONTEXT WINDOW > 95%:
- Information truncated
- Lost context
- Poor quality responses
- **You get fired when answers are incomplete**

### If COST PER QUERY > $0.05:
- Budget overrun
- Project ROI negative
- Cost kills product
- **You get fired when budget explodes**

---

## ✅ YOUR PORTFOLIO CONNECTION

### Mocktailverse shows:
- ✅ RAG implementation (grounding)
- ✅ Vector search optimization
- ✅ Chunking strategy
- ✅ Cost optimization ($1-2/month)

### AI Agent Job Intelligence shows:
- ✅ Semantic search (retrieval quality)
- ✅ Vector embeddings
- ✅ Multi-agent orchestration

### AI BI Agent shows:
- ✅ RAG implementation
- ✅ ChromaDB (vector search)
- ✅ Automated EDA

**Every GenAI question maps to these 4 pillars.**
