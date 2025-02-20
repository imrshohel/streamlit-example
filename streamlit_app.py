{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Keyword Clustering Tool V3.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/imrshohel/Keyword-Cluster/blob/main/Keyword_Clustering_Tool_V3.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "j2xQe7XNSNyf"
      },
      "source": [
        "# Keyword Clustering Tool\n",
        "This tool is created by shohel\n",
        "For contact email: imrshohel@gmail.com\n",
        "\n",
        "Automatic keyword clustering tool. See yours and your competitors most profitable keyword clusters in a couple of clicks.\n",
        "\n",
        "\n",
        "# Instructions\n",
        "Run all the cells and upload a CSV export from either:\n",
        "\n",
        "# Works with the Following Exports out the Box\n",
        "\n",
        "*   Ahrefs.com (Keyword Export / Site Explorer Export)\n",
        "*   SEMRush.com\n",
        "*   Search Console (Coverage Report CSV Export (Queries.csv))\n",
        "*   AdWords Search Terms Report .csv or Excel format (Beta)\n",
        "*   A simple single column .txt / csv file with keywords (Header or Headerless)\n",
        "\n",
        "# File Formats\n",
        "*   utf-8/utf-16/csv/xls/xlsx/xlsm/xlsb/odf/ods/odt \n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lPAaQtNdMqlb",
        "outputId": "0ec413c1-3afb-4305-da06-e42d049550f5"
      },
      "source": [
        "!pip install pandas\n",
        "!pip install polyfuzz\n",
        "!pip install chardet"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: pandas in /usr/local/lib/python3.7/dist-packages (1.1.5)\n",
            "Requirement already satisfied: python-dateutil>=2.7.3 in /usr/local/lib/python3.7/dist-packages (from pandas) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2017.2 in /usr/local/lib/python3.7/dist-packages (from pandas) (2018.9)\n",
            "Requirement already satisfied: numpy>=1.15.4 in /usr/local/lib/python3.7/dist-packages (from pandas) (1.21.3)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.7/dist-packages (from python-dateutil>=2.7.3->pandas) (1.15.0)\n",
            "Requirement already satisfied: polyfuzz in /usr/local/lib/python3.7/dist-packages (0.3.3)\n",
            "Requirement already satisfied: joblib>=0.14.0 in /usr/local/lib/python3.7/dist-packages (from polyfuzz) (1.0.1)\n",
            "Requirement already satisfied: matplotlib>=3.2.2 in /usr/local/lib/python3.7/dist-packages (from polyfuzz) (3.2.2)\n",
            "Requirement already satisfied: seaborn>=0.11.0 in /usr/local/lib/python3.7/dist-packages (from polyfuzz) (0.11.2)\n",
            "Requirement already satisfied: scikit-learn>=0.22.2.post1 in /usr/local/lib/python3.7/dist-packages (from polyfuzz) (0.22.2.post1)\n",
            "Requirement already satisfied: scipy>=1.3.1 in /usr/local/lib/python3.7/dist-packages (from polyfuzz) (1.4.1)\n",
            "Requirement already satisfied: tqdm>=4.41.1 in /usr/local/lib/python3.7/dist-packages (from polyfuzz) (4.62.3)\n",
            "Requirement already satisfied: pandas>=0.25.3 in /usr/local/lib/python3.7/dist-packages (from polyfuzz) (1.1.5)\n",
            "Requirement already satisfied: rapidfuzz>=0.13.1 in /usr/local/lib/python3.7/dist-packages (from polyfuzz) (1.8.2)\n",
            "Requirement already satisfied: numpy>=1.20.0 in /usr/local/lib/python3.7/dist-packages (from polyfuzz) (1.21.3)\n",
            "Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.7/dist-packages (from matplotlib>=3.2.2->polyfuzz) (0.10.0)\n",
            "Requirement already satisfied: kiwisolver>=1.0.1 in /usr/local/lib/python3.7/dist-packages (from matplotlib>=3.2.2->polyfuzz) (1.3.2)\n",
            "Requirement already satisfied: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.1 in /usr/local/lib/python3.7/dist-packages (from matplotlib>=3.2.2->polyfuzz) (2.4.7)\n",
            "Requirement already satisfied: python-dateutil>=2.1 in /usr/local/lib/python3.7/dist-packages (from matplotlib>=3.2.2->polyfuzz) (2.8.2)\n",
            "Requirement already satisfied: six in /usr/local/lib/python3.7/dist-packages (from cycler>=0.10->matplotlib>=3.2.2->polyfuzz) (1.15.0)\n",
            "Requirement already satisfied: pytz>=2017.2 in /usr/local/lib/python3.7/dist-packages (from pandas>=0.25.3->polyfuzz) (2018.9)\n",
            "Requirement already satisfied: chardet in /usr/local/lib/python3.7/dist-packages (3.0.4)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9GPFNiTcMZnS"
      },
      "source": [
        "import pandas as pd\n",
        "import sys\n",
        "from google.colab import files\n",
        "from polyfuzz import PolyFuzz\n",
        "import chardet\n",
        "import os"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xAjknFtjMvwJ"
      },
      "source": [
        "# rename the parent cluster name using the keyword with the highest search volume (recommended)\n",
        "parent_by_vol = True\n",
        "drop_site_links = False\n",
        "drop_image_links = False\n",
        "sim_match_percent = 0.99\n",
        "url_filter = \"\"\n",
        "min_volume = 0  # set the minimum search volume / impressions to filter on"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "resources": {
            "http://localhost:8080/nbextensions/google.colab/files.js": {
              "data": "Ly8gQ29weXJpZ2h0IDIwMTcgR29vZ2xlIExMQwovLwovLyBMaWNlbnNlZCB1bmRlciB0aGUgQXBhY2hlIExpY2Vuc2UsIFZlcnNpb24gMi4wICh0aGUgIkxpY2Vuc2UiKTsKLy8geW91IG1heSBub3QgdXNlIHRoaXMgZmlsZSBleGNlcHQgaW4gY29tcGxpYW5jZSB3aXRoIHRoZSBMaWNlbnNlLgovLyBZb3UgbWF5IG9idGFpbiBhIGNvcHkgb2YgdGhlIExpY2Vuc2UgYXQKLy8KLy8gICAgICBodHRwOi8vd3d3LmFwYWNoZS5vcmcvbGljZW5zZXMvTElDRU5TRS0yLjAKLy8KLy8gVW5sZXNzIHJlcXVpcmVkIGJ5IGFwcGxpY2FibGUgbGF3IG9yIGFncmVlZCB0byBpbiB3cml0aW5nLCBzb2Z0d2FyZQovLyBkaXN0cmlidXRlZCB1bmRlciB0aGUgTGljZW5zZSBpcyBkaXN0cmlidXRlZCBvbiBhbiAiQVMgSVMiIEJBU0lTLAovLyBXSVRIT1VUIFdBUlJBTlRJRVMgT1IgQ09ORElUSU9OUyBPRiBBTlkgS0lORCwgZWl0aGVyIGV4cHJlc3Mgb3IgaW1wbGllZC4KLy8gU2VlIHRoZSBMaWNlbnNlIGZvciB0aGUgc3BlY2lmaWMgbGFuZ3VhZ2UgZ292ZXJuaW5nIHBlcm1pc3Npb25zIGFuZAovLyBsaW1pdGF0aW9ucyB1bmRlciB0aGUgTGljZW5zZS4KCi8qKgogKiBAZmlsZW92ZXJ2aWV3IEhlbHBlcnMgZm9yIGdvb2dsZS5jb2xhYiBQeXRob24gbW9kdWxlLgogKi8KKGZ1bmN0aW9uKHNjb3BlKSB7CmZ1bmN0aW9uIHNwYW4odGV4dCwgc3R5bGVBdHRyaWJ1dGVzID0ge30pIHsKICBjb25zdCBlbGVtZW50ID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnc3BhbicpOwogIGVsZW1lbnQudGV4dENvbnRlbnQgPSB0ZXh0OwogIGZvciAoY29uc3Qga2V5IG9mIE9iamVjdC5rZXlzKHN0eWxlQXR0cmlidXRlcykpIHsKICAgIGVsZW1lbnQuc3R5bGVba2V5XSA9IHN0eWxlQXR0cmlidXRlc1trZXldOwogIH0KICByZXR1cm4gZWxlbWVudDsKfQoKLy8gTWF4IG51bWJlciBvZiBieXRlcyB3aGljaCB3aWxsIGJlIHVwbG9hZGVkIGF0IGEgdGltZS4KY29uc3QgTUFYX1BBWUxPQURfU0laRSA9IDEwMCAqIDEwMjQ7CgpmdW5jdGlvbiBfdXBsb2FkRmlsZXMoaW5wdXRJZCwgb3V0cHV0SWQpIHsKICBjb25zdCBzdGVwcyA9IHVwbG9hZEZpbGVzU3RlcChpbnB1dElkLCBvdXRwdXRJZCk7CiAgY29uc3Qgb3V0cHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKG91dHB1dElkKTsKICAvLyBDYWNoZSBzdGVwcyBvbiB0aGUgb3V0cHV0RWxlbWVudCB0byBtYWtlIGl0IGF2YWlsYWJsZSBmb3IgdGhlIG5leHQgY2FsbAogIC8vIHRvIHVwbG9hZEZpbGVzQ29udGludWUgZnJvbSBQeXRob24uCiAgb3V0cHV0RWxlbWVudC5zdGVwcyA9IHN0ZXBzOwoKICByZXR1cm4gX3VwbG9hZEZpbGVzQ29udGludWUob3V0cHV0SWQpOwp9CgovLyBUaGlzIGlzIHJvdWdobHkgYW4gYXN5bmMgZ2VuZXJhdG9yIChub3Qgc3VwcG9ydGVkIGluIHRoZSBicm93c2VyIHlldCksCi8vIHdoZXJlIHRoZXJlIGFyZSBtdWx0aXBsZSBhc3luY2hyb25vdXMgc3RlcHMgYW5kIHRoZSBQeXRob24gc2lkZSBpcyBnb2luZwovLyB0byBwb2xsIGZvciBjb21wbGV0aW9uIG9mIGVhY2ggc3RlcC4KLy8gVGhpcyB1c2VzIGEgUHJvbWlzZSB0byBibG9jayB0aGUgcHl0aG9uIHNpZGUgb24gY29tcGxldGlvbiBvZiBlYWNoIHN0ZXAsCi8vIHRoZW4gcGFzc2VzIHRoZSByZXN1bHQgb2YgdGhlIHByZXZpb3VzIHN0ZXAgYXMgdGhlIGlucHV0IHRvIHRoZSBuZXh0IHN0ZXAuCmZ1bmN0aW9uIF91cGxvYWRGaWxlc0NvbnRpbnVlKG91dHB1dElkKSB7CiAgY29uc3Qgb3V0cHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKG91dHB1dElkKTsKICBjb25zdCBzdGVwcyA9IG91dHB1dEVsZW1lbnQuc3RlcHM7CgogIGNvbnN0IG5leHQgPSBzdGVwcy5uZXh0KG91dHB1dEVsZW1lbnQubGFzdFByb21pc2VWYWx1ZSk7CiAgcmV0dXJuIFByb21pc2UucmVzb2x2ZShuZXh0LnZhbHVlLnByb21pc2UpLnRoZW4oKHZhbHVlKSA9PiB7CiAgICAvLyBDYWNoZSB0aGUgbGFzdCBwcm9taXNlIHZhbHVlIHRvIG1ha2UgaXQgYXZhaWxhYmxlIHRvIHRoZSBuZXh0CiAgICAvLyBzdGVwIG9mIHRoZSBnZW5lcmF0b3IuCiAgICBvdXRwdXRFbGVtZW50Lmxhc3RQcm9taXNlVmFsdWUgPSB2YWx1ZTsKICAgIHJldHVybiBuZXh0LnZhbHVlLnJlc3BvbnNlOwogIH0pOwp9CgovKioKICogR2VuZXJhdG9yIGZ1bmN0aW9uIHdoaWNoIGlzIGNhbGxlZCBiZXR3ZWVuIGVhY2ggYXN5bmMgc3RlcCBvZiB0aGUgdXBsb2FkCiAqIHByb2Nlc3MuCiAqIEBwYXJhbSB7c3RyaW5nfSBpbnB1dElkIEVsZW1lbnQgSUQgb2YgdGhlIGlucHV0IGZpbGUgcGlja2VyIGVsZW1lbnQuCiAqIEBwYXJhbSB7c3RyaW5nfSBvdXRwdXRJZCBFbGVtZW50IElEIG9mIHRoZSBvdXRwdXQgZGlzcGxheS4KICogQHJldHVybiB7IUl0ZXJhYmxlPCFPYmplY3Q+fSBJdGVyYWJsZSBvZiBuZXh0IHN0ZXBzLgogKi8KZnVuY3Rpb24qIHVwbG9hZEZpbGVzU3RlcChpbnB1dElkLCBvdXRwdXRJZCkgewogIGNvbnN0IGlucHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKGlucHV0SWQpOwogIGlucHV0RWxlbWVudC5kaXNhYmxlZCA9IGZhbHNlOwoKICBjb25zdCBvdXRwdXRFbGVtZW50ID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQob3V0cHV0SWQpOwogIG91dHB1dEVsZW1lbnQuaW5uZXJIVE1MID0gJyc7CgogIGNvbnN0IHBpY2tlZFByb21pc2UgPSBuZXcgUHJvbWlzZSgocmVzb2x2ZSkgPT4gewogICAgaW5wdXRFbGVtZW50LmFkZEV2ZW50TGlzdGVuZXIoJ2NoYW5nZScsIChlKSA9PiB7CiAgICAgIHJlc29sdmUoZS50YXJnZXQuZmlsZXMpOwogICAgfSk7CiAgfSk7CgogIGNvbnN0IGNhbmNlbCA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2J1dHRvbicpOwogIGlucHV0RWxlbWVudC5wYXJlbnRFbGVtZW50LmFwcGVuZENoaWxkKGNhbmNlbCk7CiAgY2FuY2VsLnRleHRDb250ZW50ID0gJ0NhbmNlbCB1cGxvYWQnOwogIGNvbnN0IGNhbmNlbFByb21pc2UgPSBuZXcgUHJvbWlzZSgocmVzb2x2ZSkgPT4gewogICAgY2FuY2VsLm9uY2xpY2sgPSAoKSA9PiB7CiAgICAgIHJlc29sdmUobnVsbCk7CiAgICB9OwogIH0pOwoKICAvLyBXYWl0IGZvciB0aGUgdXNlciB0byBwaWNrIHRoZSBmaWxlcy4KICBjb25zdCBmaWxlcyA9IHlpZWxkIHsKICAgIHByb21pc2U6IFByb21pc2UucmFjZShbcGlja2VkUHJvbWlzZSwgY2FuY2VsUHJvbWlzZV0pLAogICAgcmVzcG9uc2U6IHsKICAgICAgYWN0aW9uOiAnc3RhcnRpbmcnLAogICAgfQogIH07CgogIGNhbmNlbC5yZW1vdmUoKTsKCiAgLy8gRGlzYWJsZSB0aGUgaW5wdXQgZWxlbWVudCBzaW5jZSBmdXJ0aGVyIHBpY2tzIGFyZSBub3QgYWxsb3dlZC4KICBpbnB1dEVsZW1lbnQuZGlzYWJsZWQgPSB0cnVlOwoKICBpZiAoIWZpbGVzKSB7CiAgICByZXR1cm4gewogICAgICByZXNwb25zZTogewogICAgICAgIGFjdGlvbjogJ2NvbXBsZXRlJywKICAgICAgfQogICAgfTsKICB9CgogIGZvciAoY29uc3QgZmlsZSBvZiBmaWxlcykgewogICAgY29uc3QgbGkgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdsaScpOwogICAgbGkuYXBwZW5kKHNwYW4oZmlsZS5uYW1lLCB7Zm9udFdlaWdodDogJ2JvbGQnfSkpOwogICAgbGkuYXBwZW5kKHNwYW4oCiAgICAgICAgYCgke2ZpbGUudHlwZSB8fCAnbi9hJ30pIC0gJHtmaWxlLnNpemV9IGJ5dGVzLCBgICsKICAgICAgICBgbGFzdCBtb2RpZmllZDogJHsKICAgICAgICAgICAgZmlsZS5sYXN0TW9kaWZpZWREYXRlID8gZmlsZS5sYXN0TW9kaWZpZWREYXRlLnRvTG9jYWxlRGF0ZVN0cmluZygpIDoKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ24vYSd9IC0gYCkpOwogICAgY29uc3QgcGVyY2VudCA9IHNwYW4oJzAlIGRvbmUnKTsKICAgIGxpLmFwcGVuZENoaWxkKHBlcmNlbnQpOwoKICAgIG91dHB1dEVsZW1lbnQuYXBwZW5kQ2hpbGQobGkpOwoKICAgIGNvbnN0IGZpbGVEYXRhUHJvbWlzZSA9IG5ldyBQcm9taXNlKChyZXNvbHZlKSA9PiB7CiAgICAgIGNvbnN0IHJlYWRlciA9IG5ldyBGaWxlUmVhZGVyKCk7CiAgICAgIHJlYWRlci5vbmxvYWQgPSAoZSkgPT4gewogICAgICAgIHJlc29sdmUoZS50YXJnZXQucmVzdWx0KTsKICAgICAgfTsKICAgICAgcmVhZGVyLnJlYWRBc0FycmF5QnVmZmVyKGZpbGUpOwogICAgfSk7CiAgICAvLyBXYWl0IGZvciB0aGUgZGF0YSB0byBiZSByZWFkeS4KICAgIGxldCBmaWxlRGF0YSA9IHlpZWxkIHsKICAgICAgcHJvbWlzZTogZmlsZURhdGFQcm9taXNlLAogICAgICByZXNwb25zZTogewogICAgICAgIGFjdGlvbjogJ2NvbnRpbnVlJywKICAgICAgfQogICAgfTsKCiAgICAvLyBVc2UgYSBjaHVua2VkIHNlbmRpbmcgdG8gYXZvaWQgbWVzc2FnZSBzaXplIGxpbWl0cy4gU2VlIGIvNjIxMTU2NjAuCiAgICBsZXQgcG9zaXRpb24gPSAwOwogICAgZG8gewogICAgICBjb25zdCBsZW5ndGggPSBNYXRoLm1pbihmaWxlRGF0YS5ieXRlTGVuZ3RoIC0gcG9zaXRpb24sIE1BWF9QQVlMT0FEX1NJWkUpOwogICAgICBjb25zdCBjaHVuayA9IG5ldyBVaW50OEFycmF5KGZpbGVEYXRhLCBwb3NpdGlvbiwgbGVuZ3RoKTsKICAgICAgcG9zaXRpb24gKz0gbGVuZ3RoOwoKICAgICAgY29uc3QgYmFzZTY0ID0gYnRvYShTdHJpbmcuZnJvbUNoYXJDb2RlLmFwcGx5KG51bGwsIGNodW5rKSk7CiAgICAgIHlpZWxkIHsKICAgICAgICByZXNwb25zZTogewogICAgICAgICAgYWN0aW9uOiAnYXBwZW5kJywKICAgICAgICAgIGZpbGU6IGZpbGUubmFtZSwKICAgICAgICAgIGRhdGE6IGJhc2U2NCwKICAgICAgICB9LAogICAgICB9OwoKICAgICAgbGV0IHBlcmNlbnREb25lID0gZmlsZURhdGEuYnl0ZUxlbmd0aCA9PT0gMCA/CiAgICAgICAgICAxMDAgOgogICAgICAgICAgTWF0aC5yb3VuZCgocG9zaXRpb24gLyBmaWxlRGF0YS5ieXRlTGVuZ3RoKSAqIDEwMCk7CiAgICAgIHBlcmNlbnQudGV4dENvbnRlbnQgPSBgJHtwZXJjZW50RG9uZX0lIGRvbmVgOwoKICAgIH0gd2hpbGUgKHBvc2l0aW9uIDwgZmlsZURhdGEuYnl0ZUxlbmd0aCk7CiAgfQoKICAvLyBBbGwgZG9uZS4KICB5aWVsZCB7CiAgICByZXNwb25zZTogewogICAgICBhY3Rpb246ICdjb21wbGV0ZScsCiAgICB9CiAgfTsKfQoKc2NvcGUuZ29vZ2xlID0gc2NvcGUuZ29vZ2xlIHx8IHt9OwpzY29wZS5nb29nbGUuY29sYWIgPSBzY29wZS5nb29nbGUuY29sYWIgfHwge307CnNjb3BlLmdvb2dsZS5jb2xhYi5fZmlsZXMgPSB7CiAgX3VwbG9hZEZpbGVzLAogIF91cGxvYWRGaWxlc0NvbnRpbnVlLAp9Owp9KShzZWxmKTsK",
              "ok": true,
              "headers": [
                [
                  "content-type",
                  "application/javascript"
                ]
              ],
              "status": 200,
              "status_text": ""
            }
          },
          "base_uri": "https://localhost:8080/",
          "height": 72
        },
        "id": "9oA_ejVsPrgo",
        "outputId": "8e2b7e68-b7f4-46ae-ce20-3ec0b4a0c159"
      },
      "source": [
        "# upload the keyword export\n",
        "upload = files.upload()\n",
        "input_file = list(upload.keys())[0]  # get the name of the uploaded file\n",
        "# test the file extension\n",
        "file_extension = os.path.splitext(input_file)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-cebde99c-8dfc-4a44-b130-f44f29181d7e\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-cebde99c-8dfc-4a44-b130-f44f29181d7e\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script src=\"/nbextensions/google.colab/files.js\"></script> "
            ],
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Saving insurance claster.txt to insurance claster.txt\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2ItHhRwErGkm"
      },
      "source": [
        "# ---------------------------------- auto detect character encoding ----------------------------------------------------\n",
        "\n",
        "with open(input_file, 'rb') as rawdata:\n",
        "    result = chardet.detect(rawdata.read(10000))\n",
        "\n",
        "# if the encoding is utf-16 use a space separator, else ','\n",
        "if result['encoding'] == \"UTF-16\":\n",
        "    white_space = True\n",
        "else:\n",
        "    white_space = False\n",
        "\n",
        "if (\n",
        "    file_extension[1] == \".xlsx\"\n",
        "    or file_extension[1] == \".xls\"\n",
        "    or file_extension[1] == \".xlsm\"\n",
        "    or file_extension[1] == \".xlsb\"\n",
        "    or file_extension[1] == \".odf\"\n",
        "    or file_extension[1] == \".ods\"\n",
        "    or file_extension[1] == \".odt\"\n",
        "):\n",
        "    df_1 = pd.read_excel(input_file, engine=\"openpyxl\")\n",
        "else:\n",
        "    try:\n",
        "        df_1 = pd.read_csv(\n",
        "            input_file,\n",
        "            encoding=result[\"encoding\"],\n",
        "            delim_whitespace=white_space,\n",
        "            error_bad_lines=False,\n",
        "        )\n",
        "    # fall back to utf-8\n",
        "    except UnicodeDecodeError:\n",
        "        df_1 = pd.read_csv(\n",
        "            input_file,\n",
        "            encoding=\"utf-8\",\n",
        "            delim_whitespace=white_space,\n",
        "            error_bad_lines=False,\n",
        "        )\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Nhk1iewZrH0f"
      },
      "source": [
        "# -------------------------- check if single column import / and write header if missing -------------------------------\n",
        "\n",
        "# check the number of columns\n",
        "col_len = len(df_1.columns)\n",
        "col_name = df_1.columns[0]\n",
        "\n",
        "if col_len == 1 and df_1.columns[0] != \"Keyword\":\n",
        "    df_1.columns = [\"Keyword\"]\n",
        "\n",
        "if col_len == 1 and df_1.columns[0] != \"keyword\":\n",
        "    df_1.columns = [\"Keyword\"]\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "UBlgRin3rJw9"
      },
      "source": [
        "# -------------------------- detect if import file is adwords and remove the first two rows ----------------------------\n",
        "adwords_check = False\n",
        "if col_name == \"Search terms report\":\n",
        "    df_1.columns = df_1.iloc[1]\n",
        "    df_1 = df_1[1:]\n",
        "    df_1 = df_1.reset_index(drop=True)\n",
        "\n",
        "    new_header = df_1.iloc[0]  # grab the first row for the header\n",
        "    df_1 = df_1[1:]  # take the data less the header row\n",
        "    df_1.columns = new_header  # set the header row as the df header\n",
        "    adwords_check = True"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cv0xmvs7rNwn"
      },
      "source": [
        "# --------------------------------- Check if csv data is gsc and set bool ----------------------------------------------\n",
        "\n",
        "if 'Impressions' in df_1.columns:\n",
        "    gsc_data = True\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "kPQa5Z-qrQFH"
      },
      "source": [
        "# ----------------- standardise the column names between ahrefs v1/v2/semrush/gsc keyword exports ----------------------\n",
        "\n",
        "df_1.rename(\n",
        "    columns={\n",
        "        \"Current position\": \"Position\",\n",
        "        \"Current URL\": \"URL\",\n",
        "        \"Current URL inside\": \"Page URL inside\",\n",
        "        \"Current traffic\": \"Traffic\",\n",
        "        \"KD\": \"Difficulty\",\n",
        "        \"Keyword Difficulty\": \"Difficulty\",\n",
        "        \"Search Volume\": \"Volume\",\n",
        "        \"page\": \"URL\",\n",
        "        \"query\": \"Keyword\",\n",
        "        \"Top queries\": \"Keyword\",\n",
        "        \"Impressions\": \"Volume\",\n",
        "        \"Clicks\": \"Traffic\",\n",
        "        \"Search term\": \"Keyword\",\n",
        "        \"Impr.\": \"Volume\",\n",
        "    },\n",
        "    inplace=True,\n",
        ")"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "OGJtWEKOrQvm"
      },
      "source": [
        "# ------------------------------ check number of imported rows and warn if excessive -----------------------------------\n",
        "\n",
        "row_len = len(df_1)\n",
        "if row_len > 20_000:\n",
        "    print(\"Warning you are importing more than 20,000 keywords. If you have problems with Google Colab RAM errors, try some more pre-filtering (set minimum impressions etc)\")\n",
        "\n",
        "if col_len > 1:\n",
        "    # --------------------------------- clean the data pre-grouping ----------------------------------------------------\n",
        "\n",
        "    if url_filter:\n",
        "        print(\"Processing only URLs containing:\", url_filter)\n",
        "\n",
        "    try:\n",
        "        df_1 = df_1[df_1[\"URL\"].str.contains(url_filter, na=False)]\n",
        "    except KeyError:\n",
        "        pass\n",
        "\n",
        "    # ========================= clean strings out of numerical columns (adwords) ========================================\n",
        "\n",
        "    try:\n",
        "        df_1[\"Volume\"] = df_1[\"Volume\"].str.replace(\",\", \"\").astype(int)\n",
        "        df_1[\"Traffic\"] = df_1[\"Traffic\"].str.replace(\",\", \"\").astype(int)\n",
        "        df_1[\"Conv. value / click\"] = df_1[\"Conv. value / click\"].str.replace(\",\", \"\").astype(float)\n",
        "        df_1[\"All conv. value\"] = df_1[\"All conv. value\"].str.replace(\",\", \"\").astype(float)\n",
        "        df_1[\"CTR\"] = df_1[\"CTR\"].replace(\" --\", \"0\", regex=True)\n",
        "        df_1[\"CTR\"] = df_1[\"CTR\"].str.replace(\"\\%\", \"\").astype(float)\n",
        "        df_1[\"Cost\"] = df_1[\"Cost\"].astype(float)\n",
        "        df_1[\"Conversions\"] = df_1[\"Conversions\"].astype(int)\n",
        "        df_1[\"Cost\"] = df_1[\"Cost\"].round(2)\n",
        "        df_1[\"All conv. value\"] = df_1[\"All conv. value\"].astype(float)\n",
        "        df_1[\"All conv. value\"] = df_1[\"All conv. value\"].round(2)\n",
        "\n",
        "    except Exception:\n",
        "        pass\n",
        "\n",
        "    df_1 = df_1[~df_1[\"Keyword\"].str.contains(\"Total: \", na=False)]  # remove totals rows\n",
        "    df_1 = df_1[df_1[\"Keyword\"].notna()]  # keep only rows which are NaN\n",
        "    df_1 = df_1[df_1[\"Volume\"].notna()]  # keep only rows which are NaN\n",
        "    df_1[\"Volume\"] = df_1[\"Volume\"].astype(str)\n",
        "    df_1[\"Volume\"] = df_1[\"Volume\"].apply(lambda x: x.replace(\"0-10\", \"0\"))\n",
        "    df_1[\"Volume\"] = df_1[\"Volume\"].astype(float).astype(int)\n",
        "\n",
        "    # drop sitelinks\n",
        "\n",
        "    if drop_site_links:\n",
        "        try:\n",
        "            df_1 = df_1[~df_1[\"Page URL inside\"].str.contains(\"Sitelinks\", na=False)]  # drop sitelinks\n",
        "        except KeyError:\n",
        "            pass\n",
        "        try:\n",
        "            if gsc_data:\n",
        "                df_1 = df_1.sort_values(by=\"Traffic\", ascending=False)\n",
        "                df_1.drop_duplicates(subset=\"Keyword\", keep=\"first\", inplace=True)\n",
        "        except NameError:\n",
        "            pass\n",
        "\n",
        "    if drop_image_links:\n",
        "        try:\n",
        "            df_1 = df_1[~df_1[\"Page URL inside\"].str.contains(\"Image pack\", na=False)]  # drop image pack\n",
        "        except KeyError:\n",
        "            pass\n",
        "\n",
        "    df_1 = df_1[df_1[\"Volume\"] > min_volume]\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "LEptMghirbtA"
      },
      "source": [
        "# ------------------------------------- do the grouping ----------------------------------------------------------------\n",
        "\n",
        "df_1_list = df_1.Keyword.tolist()  # create list from df\n",
        "model = PolyFuzz(\"TF-IDF\")\n",
        "\n",
        "try:\n",
        "    model.match(df_1_list, df_1_list)\n",
        "except ValueError:\n",
        "    print(\"Empty Dataframe, Can't Match - Check the URL Filter!\")\n",
        "    sys.exit()\n",
        "\n",
        "model.group(link_min_similarity=sim_match_percent)\n",
        "\n",
        "df_matched = model.get_matches()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "OlD59vIsreG2"
      },
      "source": [
        "# ------------------------------- clean the data post-grouping ---------------------------------------------------------\n",
        "\n",
        "df_matched.rename(columns={\"From\": \"Keyword\", \"Group\": \"Cluster Name\"}, inplace=True)  # renaming multiple columns\n",
        "\n",
        "# merge keyword volume / CPC / Pos / URL etc data from original dataframe back in\n",
        "df_matched = pd.merge(df_matched, df_1, on=\"Keyword\", how=\"left\")\n",
        "\n",
        "# rename traffic (acs) / (desc) to 'Traffic for standardisation\n",
        "df_matched.rename(columns={\"Traffic (desc)\": \"Traffic\", \"Traffic (asc)\": \"Traffic\"}, inplace=True)\n",
        "\n",
        "if col_len > 1:\n",
        "\n",
        "    # fill in missing values\n",
        "    df_matched.fillna({\"Traffic\": 0, \"CPC\": 0}, inplace=True)\n",
        "    df_matched['Traffic'] = df_matched['Traffic'].round(0)\n",
        "    # ------------------------- group the data and merge in original stats -------------------------------------------------\n",
        "    if not adwords_check:\n",
        "        try:\n",
        "            # make dedicated grouped dataframe\n",
        "            df_grouped = (df_matched.groupby(\"Cluster Name\").agg(\n",
        "                {\"Volume\": sum, \"Difficulty\": \"median\", \"CPC\": \"median\", \"Traffic\": sum}).reset_index())\n",
        "        except Exception:\n",
        "            df_grouped = (df_matched.groupby(\"Cluster Name\").agg(\n",
        "                {\"Volume\": sum, \"Traffic\": sum}).reset_index())\n",
        "\n",
        "        df_grouped = df_grouped.rename(\n",
        "            columns={\"Volume\": \"Cluster Volume\", \"Difficulty\": \"Cluster KD (Median)\", \"CPC\": \"Cluster CPC (Median)\",\n",
        "                     \"Traffic\": \"Cluster Traffic\"})\n",
        "\n",
        "        df_matched = pd.merge(df_matched, df_grouped, on=\"Cluster Name\", how=\"left\")  # merge in the group stats\n",
        "\n",
        "    if adwords_check:\n",
        "\n",
        "        df_grouped = (df_matched.groupby(\"Cluster Name\").agg(\n",
        "            {\"Volume\": sum, \"CTR\": \"median\", \"Cost\": sum, \"Traffic\": sum, \"All conv. value\": sum, \"Conversions\": sum}).reset_index())\n",
        "\n",
        "        df_grouped = df_grouped.rename(\n",
        "            columns={\"Volume\": \"Cluster Volume\", \"CTR\": \"Cluster CTR (Median)\", \"Cost\": \"Cluster Cost (Sum)\",\n",
        "                     \"Traffic\": \"Cluster Traffic\", \"All conv. value\": \"All conv. value (Sum)\", \"Conversions\": \"Cluster Conversions (Sum)\"})\n",
        "\n",
        "        df_matched = pd.merge(df_matched, df_grouped, on=\"Cluster Name\", how=\"left\")  # merge in the group stats\n",
        "\n",
        "        del df_matched['To']\n",
        "        del df_matched['Similarity']\n",
        "\n",
        "    # ---------------------------- clean and sort the final output -----------------------------------------------------\n",
        "\n",
        "    try:\n",
        "        df_matched.drop_duplicates(subset=[\"URL\", \"Keyword\"], keep=\"first\", inplace=True)  # drop if both kw & url are duped\n",
        "    except KeyError:\n",
        "        pass"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "O4Svmxokri1O"
      },
      "source": [
        "\n",
        "\n",
        "if not adwords_check:\n",
        "    cols = (\n",
        "        \"Keyword\",\n",
        "        \"Cluster Name\",\n",
        "        \"Cluster Size\",\n",
        "        \"Cluster Volume\",\n",
        "        \"Cluster KD (Median)\",\n",
        "        \"Cluster CPC (Median)\",\n",
        "        \"Cluster Traffic\",\n",
        "        \"Volume\",\n",
        "        \"Difficulty\",\n",
        "        \"CPC\",\n",
        "        \"Traffic\",\n",
        "        \"URL\",\n",
        "    )\n",
        "\n",
        "    df_matched = df_matched.reindex(columns=cols)\n",
        "\n",
        "    try:\n",
        "        if gsc_data:\n",
        "            cols = \"Keyword\", \"Cluster Name\", \"Cluster Size\", \"Cluster Volume\", \"Cluster Traffic\", \"Volume\", \"Traffic\"\n",
        "            df_matched = df_matched.reindex(columns=cols)\n",
        "    except NameError:\n",
        "        pass\n",
        "\n",
        "# count cluster size\n",
        "df_matched['Cluster Size'] = df_matched['Cluster Name'].map(df_matched.groupby('Cluster Name')['Cluster Name'].count())\n",
        "\n",
        "df_matched.loc[df_matched['Cluster Size'] > 1, 'Clustered?'] = True\n",
        "df_matched['Clustered?'] = df_matched['Clustered?'].fillna(False)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Ib69NIuwrj2-"
      },
      "source": [
        "# ------------ get the keyword with the highest search volume to replace the auto generated tag name with --------------\n",
        "\n",
        "if col_len > 1:\n",
        "    if parent_by_vol:\n",
        "        df_matched['vol_max'] = df_matched.groupby(['Cluster Name'])['Volume'].transform(max)\n",
        "        # this sort is mandatory for the renaming to work properly by floating highest values to the top of the cluster\n",
        "        df_matched.sort_values([\"Cluster Name\", \"Cluster Volume\", \"Volume\"], ascending=[False, True, False], inplace=True)\n",
        "        df_matched['exact_vol_match'] = df_matched['vol_max'] == df_matched['Volume']\n",
        "        df_matched.loc[df_matched['exact_vol_match'] == True, 'highest_ranked_keyword'] = df_matched['Keyword']\n",
        "        df_matched['highest_ranked_keyword'] = df_matched['highest_ranked_keyword'].fillna(method='ffill')\n",
        "        df_matched['Cluster Name'] = df_matched['highest_ranked_keyword']\n",
        "        del df_matched['vol_max']\n",
        "        del df_matched['exact_vol_match']\n",
        "        del df_matched['highest_ranked_keyword']\n",
        "if adwords_check:\n",
        "    df_matched = df_matched.rename(columns={\"Volume\": \"Impressions\", \"Traffic\": \"Clicks\", \"Cluster Traffic\": \"Cluster Clicks (Sum)\"})\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 17
        },
        "id": "xe76sl5Vror2",
        "outputId": "84e1d93f-4dca-446b-f76c-7776aa6e348e"
      },
      "source": [
        "# -------------------------------------- final output ------------------------------------------------------------------\n",
        "# sort on cluster size\n",
        "df_matched.sort_values([\"Cluster Size\", \"Cluster Name\", \"Cluster Volume\"], ascending=[False, True, False], inplace=True)\n",
        "\n",
        "try:\n",
        "    if gsc_data:\n",
        "        df_matched.rename(\n",
        "            columns={\"Cluster Volume\": \"Cluster Impressions\", \"Cluster Traffic\": \"Cluster Clicks\", \"Traffic\": \"Clicks\",\n",
        "                     \"Volume\": \"Impressions\"}, inplace=True)\n",
        "except NameError:\n",
        "    pass\n",
        "\n",
        "if col_len == 1:\n",
        "    cols = \"Keyword\", \"Cluster Name\", \"Cluster Size\", \"Clustered?\"\n",
        "    df_matched = df_matched.reindex(columns=cols)\n",
        "\n",
        "df_matched.to_csv('your_keywords_clustered.csv', index=False)\n",
        "files.download(\"your_keywords_clustered.csv\")"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "\n",
              "    async function download(id, filename, size) {\n",
              "      if (!google.colab.kernel.accessAllowed) {\n",
              "        return;\n",
              "      }\n",
              "      const div = document.createElement('div');\n",
              "      const label = document.createElement('label');\n",
              "      label.textContent = `Downloading \"${filename}\": `;\n",
              "      div.appendChild(label);\n",
              "      const progress = document.createElement('progress');\n",
              "      progress.max = size;\n",
              "      div.appendChild(progress);\n",
              "      document.body.appendChild(div);\n",
              "\n",
              "      const buffers = [];\n",
              "      let downloaded = 0;\n",
              "\n",
              "      const channel = await google.colab.kernel.comms.open(id);\n",
              "      // Send a message to notify the kernel that we're ready.\n",
              "      channel.send({})\n",
              "\n",
              "      for await (const message of channel.messages) {\n",
              "        // Send a message to notify the kernel that we're ready.\n",
              "        channel.send({})\n",
              "        if (message.buffers) {\n",
              "          for (const buffer of message.buffers) {\n",
              "            buffers.push(buffer);\n",
              "            downloaded += buffer.byteLength;\n",
              "            progress.value = downloaded;\n",
              "          }\n",
              "        }\n",
              "      }\n",
              "      const blob = new Blob(buffers, {type: 'application/binary'});\n",
              "      const a = document.createElement('a');\n",
              "      a.href = window.URL.createObjectURL(blob);\n",
              "      a.download = filename;\n",
              "      div.appendChild(a);\n",
              "      a.click();\n",
              "      div.remove();\n",
              "    }\n",
              "  "
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "download(\"download_ed63afb5-9ffa-46a7-b9b6-d098624c891d\", \"your_keywords_clustered.csv\", 6495)"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        }
      ]
    }
  ]
}
