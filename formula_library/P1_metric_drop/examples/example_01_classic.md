# Example 1: Classic Metric Drop

**Prompt:** "Orders down 25% since yesterday. What do you do?"

1 (classic)

**Prompt:** "Orders down 25% since yesterday. What do you do?"

```text
1) Clarify
- Orders = completed checkouts? paid orders?
- Scope: all countries? web only? last 24h vs same weekday last week?
- Delta: -25% overall; when exactly started?

2) Data Check
- Any tracking/pipeline change yesterday?
- Payment event missing? order-completed event renamed?
- ETL lag: are late events missing?

3) Segment
- Slice by platform: iOS -40%, web flat
- Slice by geo: US only
=> Hot spot = iOS + US

4) Hypotheses
- iOS app update caused checkout crash
- Payment provider degraded in US iOS path
- New promo banner blocked CTA on iOS

5) Validate
- Check crash rate, latency, payment error codes by platform
- Funnel: add-to-cart ok, checkout-start ok, payment-success down
=> culprit likely payment errors / crash

6) Action
- If confirmed: rollback iOS release / switch payment fallback
- Add alerting; exec update with culprit + mitigation + monitoring
```