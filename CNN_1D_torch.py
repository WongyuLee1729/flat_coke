
import torch.nn as nn
import torch.nn.functional as F



class CNN_1D(nn.Module):
    def __init__(self):
        super(CNN_1D, self).__init__()

        self.conv1 = nn.Conv1d(1, 128, kernel_size=3)
        self.drop1 = nn.Dropout(0.3)

        self.conv2 = nn.Conv1d(128, 256, kernel_size=3)
        self.drop2 = nn.Dropout(0.3) # nn.Dropout(p=0.5)
        self.conv3 = nn.Conv1d(256, 512, kernel_size=3)

        self.drop3 = nn.Dropout(0.3)
        self.conv4 = nn.Conv1d(512, 512, kernel_size=3)

        self.fc1 = nn.Linear(43520, 512)
        self.fc2 = nn.Linear(512, 362) 


    def forward(self, x):
        x = F.relu((self.drop1(self.conv1(x)))) # conv1
        x = F.relu(F.max_pool1d(self.drop2(self.conv2(x)), 2)) # conv2
        x = F.relu(F.max_pool1d(self.drop3(self.conv3(x)), 2)) # conv3
        x = F.relu(self.conv4(x)) 
        x = x.view(-1, 43520) 
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        
        return x