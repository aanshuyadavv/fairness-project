# Fairness Project

## Notice

This repository contains work that is currently under active development as part of a collaborative research project.

The code is shared for learning and portfolio purposes only. Please do not reuse, redistribute, or include this code in other projects until the project is officially released.

---

This project uses RecBole models on the MovieLens-100K dataset to generate recommendations and compute fairness metrics.

## Models Used

* BPR
* Pop

## Dataset

* MovieLens-100K

## Project Structure

### scripts/

Contains scripts for:

* training models
* exporting recommendations
* creating item matrices

### metrics/

Contains fairness metric implementations:

* Coverage/QF using item matrix
* Coverage/QF directly from DataFrame

### outputs/

Stores generated recommendation files and item matrices.

## Recommendation Format

The recommendation DataFrame contains:

* user_id
* item_id
* rank_position
* predicted_score

## Current Metrics Implemented

* Coverage / QF

## Notes

Coverage is computed directly from the DataFrame using the number of unique recommended items divided by the total number of items in the dataset.

The total number of items is obtained directly from RecBole. Since RecBole includes a padding item (item 0), the total item count is adjusted using:

1683 - 1 = 1682 items

## Example Coverage Results

### BPR

Coverage: 0.1872

### Pop

Coverage: 0.0059

The BPR model recommends a wider variety of items, while the Pop model mainly recommends the same popular items to most users.
