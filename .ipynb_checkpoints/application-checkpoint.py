{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d0b8444f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "\n",
    "st.title(\"TJ Model Test\")\n",
    "\n",
    "st.subheader('Copy and paste input text below')\n",
    "input_text = st.text_area()\n",
    "\n",
    "st.subheader('Review results here')\n",
    "green_job = True if 'climate' in input_text else False\n",
    "st.text(f'Green Job : {green_job}')\n",
    "\n",
    "choice = st.radio(\"Pick one\", [\"Good\",\"Bad\"])\n"
   ]
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
   "version": "3.9.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
