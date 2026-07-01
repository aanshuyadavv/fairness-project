# Fairness Project

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
