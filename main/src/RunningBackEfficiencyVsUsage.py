import pandas
import seaborn
from matplotlib import pyplot
from util import scoringutil

# Import CSV
df = pandas.read_csv('../resources/PFR-2019.csv')

# Formatting
df.drop(['Rk', '2PM', '2PP', 'FantPt', 'DKPt', 'FDPt', 'VBD', 'PosRank', 'OvRank', 'PPR', 'Fmb', 'GS'], axis=1,
        inplace=True)
df['Player'] = df['Player'].apply(lambda x: x.split('*')[0]).apply(lambda x: x.split('\\')[0])
df.rename({
    'TD': 'PassingTD',
    'TD.1': 'RushingTD',
    'TD.2': 'ReceivingTD',
    'TD.3': 'TotalTD',
    'Yds': 'PassingYds',
    'Yds.1': 'RushingYds',
    'Yds.2': 'ReceivingYds',
    'Att': 'PassingAtt',
    'Att.1': 'RushingAtt'
}, axis=1, inplace=True)
rb_df = df[df['FantPos'] == 'RB']
qb_df = df[df['FantPos'] == 'QB']
wr_df = df[df['FantPos'] == 'WR']
te_df = df[df['FantPos'] == 'TE']

# New columns for usage
rb_df['FantasyPoints'] = scoringutil.calculateSimpleScore(rb_df['RushingYds'], rb_df['RushingTD'], rb_df['RushingAtt'],
                                                          rb_df['ReceivingYds'], rb_df['ReceivingTD'], rb_df['Rec'])

rb_df['FantasyPoints/Game'] = rb_df['FantasyPoints'] / rb_df['G']
rb_df['FantasyPoints/Game'] = rb_df['FantasyPoints/Game'].apply(lambda x: round(x, 2))

rb_df['Usage/Game'] = (rb_df['RushingAtt'] + rb_df['Tgt']) / rb_df['G']
rb_df['Usage/Game'] = rb_df['Usage/Game'].apply(lambda x: round(x, 2))

# Create plot
seaborn.set_style('whitegrid')
fig, ax = pyplot.subplots()
fig.set_size_inches(15, 10)

plot = seaborn.regplot(
    x=rb_df['Usage/Game'],
    y=rb_df['FantasyPoints/Game'],
    scatter=True
)

# New column for efficiency
rb_df['TD/Usage'] = (rb_df['RushingTD']+rb_df['ReceivingTD'])/(rb_df['RushingAtt']+rb_df['Tgt'])

# Create plot
fig, ax = pyplot.subplots()
fig.set_size_inches(15, 10)

# Sample size
rb_df = rb_df[rb_df['RushingAtt'] > 20]

plot = seaborn.regplot(
    x=rb_df['TD/Usage'],
    y=rb_df['FantasyPoints/Game'],
    scatter=True
)