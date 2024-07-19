# water_marking_system_buildspace_s5

# Imagine Hashing

## Team
- **Kshitij Koushik Kota**: [GitHub](https://github.com/kshitijkota)
- **Pranav Hemanth**: [GitHub](https://github.com/pranavhemanth)
- **Sampriti Saha**: [GitHub](https://github.com/sampritimaha)
- **Pranav Rajesh Narayan**: [GitHub](https://github.com/pranavrajesh)
- **Roshini Ramesh**: [GitHub](https://github.com/roshiniramesh)

## Introduction
**Topic:** Digital Watermarking of Images

In the AI-driven media landscape, digital forgery, deep fakes, copyright infringement, and plagiarism present significant challenges. Verifying the originality and integrity of images is essential to combat misinformation and protect intellectual property. This documentation provides a comprehensive overview of our digital watermarking system designed to authenticate images by embedding hashes. The system maintains image integrity and authenticity, even through compressions and data transfers.

## Problem Statement
Images on the internet have become a significant source of misinformation, posing challenges for authenticity verification. Current watermarking methods are inadequate, lacking the ability to effectively mark images from their inception. This deficiency allows for the dissemination of altered or misleading content, undermining trust in digital media.

## Objective
Develop a robust watermarking system for raw images that can be embedded at the image's inception. This system will enable any individual on the internet to verify if an image is unaltered or has been tampered with.

## Scope
- **Imperceptible yet robust watermarks**: Embed watermarks into images that withstand common manipulations.
- **Compatibility**: Support a wide range of image formats.
- **Verification**: Provide an online platform for easy verification of watermarked images.
- **Scalability**: Ensure the system can adapt to future advancements in AI and image processing.

## Key Features
- **Embedding at Creation**: Watermarks are embedded at the point of image creation.
- **Imperceptibility**: Watermarks are invisible to the human eye but resistant to tampering.
- **Format Compatibility**: Supports various image formats and resolutions.
- **Easy Verification**: Accessible online verification process.
- **Scalability**: Designed to handle large-scale usage and advancements in technology.

## Beneficiaries
- **Content Creators and Artists**: Protect original work from unauthorized use.
- **Media Organizations and Journalists**: Verify authenticity of news images.
- **Social Media Platforms**: Curb misinformation.
- **General Internet Users**: Verify image authenticity online.

## Outcome
An effective watermarking system for AI-generated images will combat misinformation, protect intellectual property rights, and foster trust in digital media.

## Drawbacks of Current Watermarking Methods
- Ease of Removal: Watermarks are easily removed by advanced AI algorithms.
- Image Quality: Watermarks can degrade image quality.
- Limited Robustness: Vulnerable to common image processing operations.
- Detection Complexity: Computationally intensive verification.
- Limited Compatibility: May not work with all image types or require specific software.
- Content Creator Overhead: Time-consuming and resource-intensive.
- User Experience: Watermarks can interfere with viewing experience.
- Risk of Alteration: Watermarks can be altered or removed.

## Solution
### System Description
**Purpose**: Authenticate images by embedding a unique hash as a digital watermark, ensuring originality and verification.

#### Image Generation or Capturing
- **Technology**: Use AI platforms like DALL-E for high-quality image generation or standard cameras for capturing raw images.
- **Process**: Generate or capture images based on user inputs or predefined criteria.

#### Hash Embedding
- **Timing**: Embed the hash at the final layer of image generation or capturing.
- **Method**: Derive a hash from the image properties and embed it as a digital watermark.

#### Attention Algorithm
- **Purpose**: Identify optimal locations for hash embedding.
- **Functionality**: Recognize significant areas in the image that are less prone to distortion/compression.

#### Embedding Technique
- **Current Method**: Use LSB substitution to embed the hash.
- **Extraction**: Reverse the embedding process to retrieve the hash.
- **Authentication**: Utilize the embedded hashes to verify image authenticity.

By combining these steps, our solution provides a coherent and reliable method for ensuring image authenticity, making it a valuable tool in combating misinformation and verifying digital content.

### Detailed Solution Approach
#### Step 1: Object Identification and Attention Algorithm
**Object Identification**
- **Objective**: Identify objects within images, such as animals, landscapes, and humans.
- **Method**: Employ convolutional neural networks (CNNs) trained on labeled image datasets for accurate object detection.

**Attention Algorithm**
- **Objective**: Determine the critical parts of an image that are optimal for hash embedding.
- **Method**: Use the ML model to segment the image into its constituent parts and identify areas that are less likely to be altered or distorted.

#### Step 2: Steganography Embedding with Hashing
**Hash Generation**
- **Objective**: Create a unique identifier for each image.
- **Method**: Generate a hash using the SHA256 hashing algorithm based on the image's properties.

**Hash Embedding**
- **Objective**: Embed the hash into the image in a manner that is imperceptible to the human eye.
- **Method**:
  - Utilize the attention algorithm to pinpoint optimal embedding coordinates.
  - Embed the hash using Least Significant Bit (LSB) embedding techniques.

### Verification Process
1. **Extract the Embedded Hash**: Use the same coordinates and techniques to retrieve the hash from the image.
2. **Compute the Hash Independently**: Generate a hash using SHA256 on the current state of the image.
3. **Match the Hashes**: Compare the extracted hash with the independently computed hash to verify the image's integrity.

### Benefits
- **Robust Verification**: Ensures the authenticity of images through a secure embedding process.
- **Imperceptible Watermarks**: Embedding is done in a manner that is invisible to the human eye, resistant to tampering.
- **Independent Verification**: Allows any user to verify image authenticity without specialized tools.

## Main Problems and Solutions
### How to Embed the Hash
- **Current Solution**: Use simple LSB substitution.
- **Future Enhancements**: Explore frequency-based methods and combine with LSB for robustness.

### How to Make the Hash Persist
- **Strategy**: Embed in areas less prone to compression, such as edges, low-frequency areas, color channels, salient features, key points, and descriptors.
- **Initial Implementation**: Use PNG format for stable embedding.

### Where to Embed the Hash
- **Attention Algorithm**: Identify least altering areas for embedding.

### What Information to Embed
- **Current Data**: Embed SHA256 hash of the image.
- **Additional Data**: Embed source and related information.

### Who Should Have Access
- **Initial Release**: Large companies first.
- **Staggered Release**: Gradually extend to smaller companies.
- **Future Expansion**: Make accessible to individual users.

## Definitions
- **Raw Images**: Unprocessed images at the source of inception (e.g., camera pictures, AI-generated images).

## References and Similar Research
- [Meta's Solution - Stable Signatures](https://example.com)
- [Google DeepMind Watermarking Tool](https://example.com)
- [AI Watermarks on DALL-E](https://example.com)
- [Internals of Image Steganography - Codementor](https://www.codementor.io/arpitbhayani/internals-of-image-steganography-12qsxcxjsh)
- [How does Syndrome-Trellis Code (STC) work? - Cryptography Stack Exchange](https://crypto.stackexchange.com)
- [Detection of tamper forgery image in security digital image - ScienceDirect](https://www.sciencedirect.com)
- [Image Tampering - ScienceDirect](https://www.sciencedirect.com)
- [Digital Steganography and Watermarking for Digital Images: A Review of Current Research Directions | IEEE Journals & Magazine | IEEE Xplore](https://ieeexplore.ieee.org)
- [A New Approach of Steganography on Image Metadata | Fernando | JOIV](https://www.joiv.org)
- [A Survey of Image Steganography Techniques - ResearchGate](https://www.researchgate.net)
- [The Stable Signature: Rooting Watermarks in Latent Diffusion Models - arXiv](https://arxiv.org/abs/2303.15435)
- [A blind spatial domain-based image watermarking using texture analysis and association rules mining - ResearchGate](https://www.researchgate.net)
- [ARM Controller Based Image Steganography Using LSB Algorithm - ResearchGate](https://www.researchgate.net)
- [A New Method of Image Steganography Using 7th Bit of a Pixel as Indicator by Introducing the Successive Temporary Pixel in the Gray Scale Image - ResearchGate](https://www.researchgate.net)
- [Securing and Hiding Secret Message in Image using XOR Transposition Encryption and LSB Method - IOPscience](https://iopscience.iop.org)
- [Understanding DCT and Quantization in JPEG compression - DEV Community](https://dev.to)
- [How are Images Compressed?  [46MB ↘↘ 4.07MB] JPEG In Depth - YouTube](https://www.youtube.com)
- [JPEG DCT, Discrete Cosine Transform (JPEG Pt2)- Computerphile - YouTube](https://www.youtube.com)
- [How Computers Compress Text: Huffman Coding and Huffman Trees -YouTube](https://www.youtube.com)

