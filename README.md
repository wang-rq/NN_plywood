# Plywood counter

The project provide counting of sheets in stack of plywood based on photo of stack. 

## Solution

As base architecture for convolutional neural network the AlexNet architecture was choosen. The AlexNet was extended by adding several fully connected layers. In overall the 8 proposed models was selected and tested. 

| Model Version | Additional layers                                                                                                                                   | Train data  | Loss function | Average error |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------|-------------|---------------|---------------|
| 1             | nn.Linear(in_features=4096, out_features=4096),<br>nn.Linear(in_features=4096, out_features=1024),<br>nn.Linear(in_features=1024, out_features=1) | Merged | MSE           | 0.3102743761  |
| 2             | nn.Linear(in_features=4096, out_features=4096),<br>nn.Linear(in_features=4096, out_features=1)                                                    | Merged      | MSE           | 0.356755558   |
| 3             | nn.Linear(in_features=4096, out_features=4096),<br>nn.Linear(in_features=4096, out_features=2048),<br>nn.Linear(in_features=2048, out_features=1) | Merged      | MSE           | 0.3254900442  |
| 4             | nn.Linear(in_features=4096, out_features=4096),<br>nn.Linear(in_features=4096, out_features=1024),<br>nn.Linear(in_features=1024, out_features=1) | Merged      | Smooth L1     | 0.3906039606  |
| 5             | nn.Linear(in_features=4096, out_features=4096),<br>nn.Linear(in_features=4096, out_features=1024),<br>nn.Linear(in_features=1024, out_features=1) | Original    | Smooth L1     | 0.1566808731  |
| 6             | nn.Linear(in_features=4096, out_features=1)                                                                                                       | Merged      | Smooth L1     | 0.4553910928  |
| 7             | nn.Linear(in_features=4096, out_features=4096),<br>nn.Linear(in_features=4096, out_features=2048),<br>nn.Linear(in_features=2048, out_features=1) | Merged      | Smooth L1     | 0.4294855982  |
| 8             | nn.Linear(in_features=4096, out_features=1024),<br>nn.Linear(in_features=1024, out_features=1)                                                | Merged      | Smooth L1     | 0.4225038808  |

*Merged data - data containing cropped images of original images*.

As result version 5 of proposed model was choosen. 