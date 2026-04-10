{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "3904f956",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "\n",
    "def sum_squares_error(y,t):\n",
    "    return 0.5*(np.sum((y-t)**2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "390155ab",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.float64(0.09750000000000003)"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "t = [0,0,1,0,0,0,0,0,0,0]\n",
    "y = [0.1,0.05,0.6,0.0,0.05,0.1,0.0,0.1,0.0,0.0]\n",
    "sum_squares_error(np.array(y),np.array(t))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "85187f69",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.float64(0.5975)"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y = [0.1,0.05,0.1,0.0,0.05,0.1,0.0,0.6,0.0,0.0]\n",
    "sum_squares_error(np.array(y),np.array(t))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "2e7a3cdd",
   "metadata": {},
   "outputs": [],
   "source": [
    "def cross_entropy_error(y,t):\n",
    "    delta = 1e-7\n",
    "    return -np.sum(t * np.log(y + delta))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "3a89d747",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.float64(0.510825457099338)"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "t = [0,0,1,0,0,0,0,0,0,0]\n",
    "y = [0.1,0.05,0.6,0.0,0.05,0.1,0.0,0.1,0.0,0.0]\n",
    "cross_entropy_error(np.array(y),np.array(t))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "ce83efca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.float64(2.302584092994546)"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y = [0.1,0.05,0.1,0.0,0.05,0.1,0.0,0.6,0.0,0.0]\n",
    "cross_entropy_error(np.array(y),np.array(t))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "50b4ccb2",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
