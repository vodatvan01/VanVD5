import numpy as np


# 2a
def triplet_loss(anchor, positive, negative, alpha=0.2):
    """
    Tính toán triplet loss.
    
    Parameters:
    - anchor: numpy array, vector đặc trưng của anchor.
    - positive: numpy array, vector đặc trưng của positive.
    - negative: numpy array, vector đặc trưng của negative.
    - alpha: float, margin.

    Returns:
    - loss: float, giá trị của triplet loss.
    """
    pos_dist = np.sum((anchor - positive) ** 2)
    neg_dist = np.sum((anchor - negative) ** 2)
    
    # Tính triplet loss
    loss = np.maximum(0, pos_dist - neg_dist + alpha)
    
    return loss


# 2b
def extended_triplet_loss(anchor, positives, negatives, alpha=0.2):
    """
    Tính toán triplet loss mở rộng với nhiều mẫu positive và negative.
    
    Parameters:
    - anchor: numpy array, vector đặc trưng của anchor.
    - positives: numpy array, ma trận đặc trưng của các mẫu positive.
    - negatives: numpy array, ma trận đặc trưng của các mẫu negative.
    - alpha: float, margin.

    Returns:
    - loss: float, giá trị của triplet loss.
    """
    loss = 0.0
    
    # Tính toán loss cho tất cả các cặp (anchor, positive, negative)
    for p in positives:
        for n in negatives:
            loss += triplet_loss(anchor,p,n, alpha)
    return loss

# Ví dụ
anchor = np.array([0.5, 0.5])
positives = np.array([[0.6, 0.6], [0.55, 0.55]])
negatives = np.array([
    [1.0, 1.0],
    [0.9, 0.9],
    [1.1, 1.1],
    [1.2, 1.2],
    [0.8, 0.8]
])

loss = extended_triplet_loss(anchor, positives, negatives)
print(f"Extended Triplet loss: {loss}")
