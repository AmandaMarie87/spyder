{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPr5CBiX9C+fU8CeFBATvm/",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
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
        "<a href=\"https://colab.research.google.com/github/AmandaMarie87/spyder/blob/master/Files_AssignmentCYSE250.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Function to duplicate lines from input file to output file\n",
        "def duplicate_lines(input_file, output_file):\n",
        "    try:\n",
        "        # Open the input file for reading and output file for writing\n",
        "        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:\n",
        "            for line in infile:\n",
        "                # Write each line twice in the output file\n",
        "                outfile.write(line)\n",
        "                outfile.write(line)\n",
        "        print(f\"Lines duplicated successfully into '{output_file}'!\")\n",
        "    except FileNotFoundError:\n",
        "        print(f\"Error: The file '{input_file}' does not exist.\")\n",
        "    except Exception as e:\n",
        "        print(f\"An error occurred: {e}\")\n",
        "\n",
        "# Sample usage\n",
        "if __name__ == \"__main__\":\n",
        "    input_file = \"input1.txt\"  # Name of the input file\n",
        "    output_file = \"output1.txt\"  # Name of the output file\n",
        "\n",
        "    # Create a sample input file for demonstration\n",
        "    with open(input_file, 'w') as f:\n",
        "        f.write(\"Python is amazing.\\n\")\n",
        "        f.write(\"I like programming a lot.\\n\")\n",
        "\n",
        "    # Call the function to duplicate lines\n",
        "    duplicate_lines(input_file, output_file)\n",
        "\n",
        "    # Displaying the content of the output file\n",
        "    with open(output_file, 'r') as f:\n",
        "        print(\"\\nOutput File Content:\")\n",
        "        print(f.read())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jbK_ueg-gWM_",
        "outputId": "168c3adc-09ba-427e-d8fc-29aed89ca428"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Lines duplicated successfully into 'output1.txt'!\n",
            "\n",
            "Output File Content:\n",
            "Python is amazing.\n",
            "Python is amazing.\n",
            "I like programming a lot.\n",
            "I like programming a lot.\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Function to calculate the square of a number\n",
        "def square_number(number):\n",
        "    return number ** 2\n",
        "\n",
        "# Input and output file names\n",
        "input_file_name = \"input.txt\"\n",
        "output_file_name = \"output.txt\"\n",
        "\n",
        "try:\n",
        "    # Open the input file for reading\n",
        "    with open(input_file_name, \"r\") as input_file:\n",
        "        # Read the numbers from the input file\n",
        "        numbers = [int(line.strip()) for line in input_file.readlines()]\n",
        "\n",
        "    # Calculate the squares of the numbers\n",
        "    squares = [square_number(number) for number in numbers]\n",
        "\n",
        "    # Open the output file for writing\n",
        "    with open(output_file_name, \"w\") as output_file:\n",
        "        # Write the squares to the output file\n",
        "        for square in squares:\n",
        "            output_file.write(str(square) + \"\\n\")\n",
        "\n",
        "    print(f\"Squares written to {output_file_name}\")\n",
        "\n",
        "except FileNotFoundError:\n",
        "    print(f\"Error: {input_file_name} not found.\")\n",
        "except Exception as e:\n",
        "    print(f\"An error occurred: {str(e)}\")"
      ],
      "metadata": {
        "id": "FtEm1OvekbGE",
        "outputId": "4a4b7d65-695d-42bf-8718-89fd56b2379e",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Squares written to output.txt\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "first_names = open('firstnames.txt', 'r').readlines()\n",
        "last_names = open('lastnames.txt', 'r').readlines()\n",
        "full_names = [first_name.strip() + ' ' + last_name for first_name, last_name in zip(first_names, last_names)]\n",
        "with open('fullnames.txt', 'w') as f:\n",
        "    for name in full_names:\n",
        "        f.write(name + '\\n')"
      ],
      "metadata": {
        "id": "K6RmTYY5kpNy"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def read_grades(input_file):\n",
        "    with open(input_file, 'r') as file:\n",
        "        lines = file.readlines()\n",
        "    return [line.strip() for line in lines]\n",
        "\n",
        "def calculate_mean_grades(grades):\n",
        "    mean_grades = []\n",
        "    for grade_line in grades:\n",
        "        grade_values = list(map(int, grade_line.split()))\n",
        "        mean_grade = sum(grade_values) // len(grade_values)\n",
        "        mean_grades.append(mean_grade)\n",
        "    return mean_grades\n",
        "\n",
        "def write_mean_grades(output_file, mean_grades):\n",
        "    with open(output_file, 'w') as file:\n",
        "        for mean_grade in mean_grades:\n",
        "            file.write(f\"{mean_grade}\\n\")\n",
        "\n",
        "def main(input_file, output_file):\n",
        "    grades = read_grades(input_file)\n",
        "    mean_grades = calculate_mean_grades(grades)\n",
        "    write_mean_grades(output_file, mean_grades)\n",
        "\n",
        "# Specify the input and output file names\n",
        "input_file = 'inputgrades.txt'\n",
        "output_file = 'outputgrades.txt'\n",
        "\n",
        "# Execute the main function\n",
        "main(input_file, output_file)"
      ],
      "metadata": {
        "id": "6PvG9VHtqRLL"
      },
      "execution_count": 31,
      "outputs": []
    }
  ]
}