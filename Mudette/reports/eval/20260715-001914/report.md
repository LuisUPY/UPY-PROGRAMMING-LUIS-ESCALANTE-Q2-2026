# MTGuard — Reporte de evaluación no circular

Split: **dev** · Generado: 2026-07-15T00:19:14

Ground truth = etiqueta de procedencia del escenario, nunca la salida del detector. FLAG = veredicto máximo ≥ ALERT · BLOCK = ≥ CONTAIN (incluye judge DENY).

## Ablación por configuración

| Config | recall@FLAG | recall@BLOCK | FP@FLAG | FP@BLOCK | prec@FLAG | Δrecall@FLAG vs l1_only |
|---|---|---|---|---|---|---|
| l1_only | 80.0% | 80.0% | 0.0% | 0.0% | 100.0% | — |
| l2_only | 0.0% | 0.0% | 0.0% | 0.0% | n/a | -80.0pp |
| l1_l2 | 82.9% | 80.0% | 0.0% | 0.0% | 100.0% | +2.9pp |

**Valor incremental de la trayectoria:** 1/35 ataques FLAGgeados por L1+L2 que L1 solo NO detectó: `['leg_a26']`

## Atribución de factores en el primer FLAG (¿quién hace el trabajo?)

**l1_only**: `l1_high` 100.0%

**l2_only**: sin FLAGs

**l1_l2**: `l1_high` 96.5% · `trajectory_high` 89.7% · `proximity_high` 72.4% · `escalation` 6.9% · `l1_medium` 3.5%

## Desglose por categoría

### l1_only

| Categoría | n | recall@FLAG | recall@BLOCK | FP@FLAG |
|---|---|---|---|---|
| benign_support | 44 | n/a | n/a | 0.0% |
| crescendo | 1 | 100.0% | 100.0% | n/a |
| direct_probe | 32 | 78.1% | 78.1% | n/a |
| jailbreak | 1 | 100.0% | 100.0% | n/a |
| salami | 1 | 100.0% | 100.0% | n/a |

### l2_only

| Categoría | n | recall@FLAG | recall@BLOCK | FP@FLAG |
|---|---|---|---|---|
| benign_support | 44 | n/a | n/a | 0.0% |
| crescendo | 1 | 0.0% | 0.0% | n/a |
| direct_probe | 32 | 0.0% | 0.0% | n/a |
| jailbreak | 1 | 0.0% | 0.0% | n/a |
| salami | 1 | 0.0% | 0.0% | n/a |

### l1_l2

| Categoría | n | recall@FLAG | recall@BLOCK | FP@FLAG |
|---|---|---|---|---|
| benign_support | 44 | n/a | n/a | 0.0% |
| crescendo | 1 | 100.0% | 100.0% | n/a |
| direct_probe | 32 | 81.2% | 78.1% | n/a |
| jailbreak | 1 | 100.0% | 100.0% | n/a |
| salami | 1 | 100.0% | 100.0% | n/a |

## Detección temprana (ataques multi-turn)

| Config | mediana del primer FLAG (turno, 0-idx) |
|---|---|
| l1_only | 3.5 |
| l2_only | None |
| l1_l2 | 3.5 |

## Limitaciones declaradas

- Los escenarios `legacy`/`legacy_playbook` fueron escritos por los autores del detector: viven solo en dev y no sustentan afirmaciones de generalización.
- Las fuentes externas (cuando estén integradas) son de dominio genérico; las regiones L2 del pack son específicas de IT — leer las métricas por fuente, no solo el agregado.
- CI no impone bandas de recall (anti-circularidad); el número se reporta, no se garantiza.

## Procedencia (manifest)

```json
{
 "version": 1,
 "created": "2026-07-15",
 "protocol": {
  "ground_truth": "label = procedencia del caso (attack/benign por origen); la salida del detector jamas etiqueta",
  "splits": {
   "dev": "tuning de umbrales y seleccion de variantes permitidos",
   "test": "CONGELADO al crearse (Phase 9.2, fuentes externas); solo run-to-report, prohibido iterar contra el"
  },
  "operating_points": {
   "FLAG": "max verdict >= ALERT",
   "BLOCK": "max verdict >= CONTAIN o judge DENY"
  },
  "ci_policy": "sin bandas de recall en CI (anti-circularidad R2#3); solo invariantes de FP en benignos faciles",
  "legacy_rule": "todo caso self-authored vive en dev; el test set lo dominan fuentes externas"
 },
 "sources": {
  "legacy": {
   "description": "corpus single-turn original (attacks.json/benign.json)",
   "license": "self-authored",
   "split": "dev"
  },
  "legacy_playbook": {
   "description": "playbooks demo multi-turn (attack/benign_playbook.json)",
   "license": "self-authored",
   "split": "dev"
  }
 },
 "test_freeze": null,
 "sha256": {
  "attacks_dev.json": "066bd80adef2c9982cd072c702b4eeca430c4fb156e19c61b9a6518e6568ed23",
  "benign_dev.json": "35660747f66735c17e2c39f60bc6325ad236a2aa20976e2f2a5e631e46a66e96"
 }
}
```
