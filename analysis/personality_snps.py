# Comprehensive database of personality-related SNPs
# Based on peer-reviewed genetic association studies

PERSONALITY_SNPS = {
    # ============================================================================
    # SEROTONIN SYSTEM - Mood, anxiety, emotional regulation
    # ============================================================================

    # SLC6A4 (5-HTTLPR) - Serotonin Transporter
    "rs25531": {
        "gene": "SLC6A4",
        "name": "Serotonin Transporter Promoter",
        "chromosome": "17",
        "function": "Regulates serotonin reuptake efficiency in synapses",
        "category": "Serotonin System",
        "variants": {
            "AA": {
                "effect": "Low expression variant (S/S equivalent)",
                "traits": "Higher emotional sensitivity, increased stress reactivity, deeper emotional processing. May experience more intense emotional responses to both positive and negative events. Associated with heightened empathy and environmental sensitivity.",
                "detail": "The low-expression variant results in less efficient serotonin reuptake, leading to more serotonin remaining in synaptic clefts. This creates heightened sensitivity to emotional stimuli and environmental factors."
            },
            "AG": {
                "effect": "Intermediate expression (L/S equivalent)",
                "traits": "Balanced emotional sensitivity with moderate stress resilience. Combines emotional depth with reasonable coping mechanisms.",
                "detail": "Heterozygous individuals show intermediate serotonin transporter expression, providing a balance between emotional sensitivity and resilience."
            },
            "GG": {
                "effect": "High expression variant (L/L equivalent)",
                "traits": "Greater emotional resilience, lower anxiety predisposition, more stable mood regulation. Better stress coping but potentially less sensitive to subtle emotional cues.",
                "detail": "High expression leads to efficient serotonin clearance, associated with more stable emotional baseline and reduced susceptibility to environmental stressors."
            }
        },
        "interactions": ["rs6295", "rs1800532", "rs4680"],
        "references": ["Caspi et al. 2003 Science", "Karg et al. 2011 Arch Gen Psychiatry"]
    },

    "rs6295": {
        "gene": "HTR1A",
        "name": "Serotonin Receptor 1A",
        "chromosome": "5",
        "function": "Primary inhibitory serotonin receptor affecting mood and anxiety",
        "category": "Serotonin System",
        "variants": {
            "CC": {
                "effect": "Reduced receptor expression",
                "traits": "Increased susceptibility to anxiety and depression. More intense negative emotional responses. Higher baseline arousal states.",
                "detail": "Lower 5-HT1A receptor density in limbic regions leads to reduced inhibitory control over stress responses."
            },
            "CG": {
                "effect": "Intermediate expression",
                "traits": "Moderate anxiety sensitivity with functional emotional regulation.",
                "detail": "Balanced receptor expression provides adequate serotonergic inhibitory tone."
            },
            "GG": {
                "effect": "Higher receptor expression",
                "traits": "Natural resilience to anxiety, calmer baseline temperament, better mood stability.",
                "detail": "Increased 5-HT1A autoreceptor function provides stronger negative feedback on serotonin release, promoting emotional equilibrium."
            }
        },
        "interactions": ["rs25531", "rs6311"],
        "references": ["Lemonde et al. 2003 J Neurosci", "Strobel et al. 2003 Mol Psychiatry"]
    },

    "rs6311": {
        "gene": "HTR2A",
        "name": "Serotonin Receptor 2A",
        "chromosome": "13",
        "function": "Major excitatory serotonin receptor involved in cognition and perception",
        "category": "Serotonin System",
        "variants": {
            "AA": {
                "effect": "Lower receptor density",
                "traits": "Potentially reduced responsiveness to emotional stimuli, different cognitive processing patterns.",
                "detail": "Reduced 5-HT2A density may affect cortical processing of emotional and sensory information."
            },
            "AG": {
                "effect": "Intermediate expression",
                "traits": "Balanced serotonergic signaling in cortical regions.",
                "detail": "Moderate receptor density providing standard emotional and cognitive processing."
            },
            "GG": {
                "effect": "Higher receptor density",
                "traits": "Enhanced emotional perception, potentially more vivid imagination, stronger response to emotional stimuli.",
                "detail": "Increased 5-HT2A receptor availability may enhance cortical processing of sensory and emotional information."
            }
        },
        "interactions": ["rs6295", "rs25531"],
        "references": ["Polesskaya & Bhardwaj 2005", "Turecki et al. 1999"]
    },

    "rs1800532": {
        "gene": "TPH1",
        "name": "Tryptophan Hydroxylase 1",
        "chromosome": "11",
        "function": "Rate-limiting enzyme in peripheral serotonin synthesis",
        "category": "Serotonin System",
        "variants": {
            "AA": {
                "effect": "Standard enzyme activity",
                "traits": "Normal serotonin production patterns.",
                "detail": "Typical tryptophan hydroxylase function supporting baseline serotonin synthesis."
            },
            "AC": {
                "effect": "Intermediate activity",
                "traits": "Slightly altered serotonin synthesis dynamics.",
                "detail": "Heterozygous state may show subtle variations in serotonin availability."
            },
            "CC": {
                "effect": "Altered enzyme kinetics",
                "traits": "Associated with increased emotional intensity and potentially higher harm avoidance.",
                "detail": "This variant has been linked to altered serotonergic tone and emotional processing differences."
            }
        },
        "interactions": ["rs25531", "rs4570625"],
        "references": ["Nielsen et al. 1994", "Rujescu et al. 2003"]
    },

    "rs4570625": {
        "gene": "TPH2",
        "name": "Tryptophan Hydroxylase 2",
        "chromosome": "12",
        "function": "Brain-specific serotonin synthesis enzyme",
        "category": "Serotonin System",
        "variants": {
            "GG": {
                "effect": "Standard brain serotonin synthesis",
                "traits": "Normal emotional regulation capacity, typical stress responses.",
                "detail": "Normal TPH2 activity supporting adequate central serotonin production."
            },
            "GT": {
                "effect": "Moderately reduced synthesis",
                "traits": "Somewhat increased emotional sensitivity, may show stronger reactions to stress.",
                "detail": "Reduced enzyme efficiency may lead to lower central serotonin availability under stress."
            },
            "TT": {
                "effect": "Reduced serotonin synthesis capacity",
                "traits": "Higher emotional reactivity, increased vulnerability to mood disturbances under stress, more intense emotional experiences.",
                "detail": "Significantly reduced TPH2 activity has been associated with altered emotional processing and increased stress sensitivity."
            }
        },
        "interactions": ["rs25531", "rs1800532"],
        "references": ["Zhang et al. 2005 Neuron", "Chen et al. 2008"]
    },

    # ============================================================================
    # DOPAMINE SYSTEM - Reward, motivation, executive function
    # ============================================================================

    "rs4680": {
        "gene": "COMT",
        "name": "Catechol-O-Methyltransferase Val158Met",
        "chromosome": "22",
        "function": "Primary enzyme for dopamine degradation in prefrontal cortex",
        "category": "Dopamine System",
        "variants": {
            "AA": {
                "effect": "Met/Met - Low COMT activity (Worrier)",
                "traits": "Higher prefrontal dopamine levels. Enhanced working memory, better cognitive performance under low stress, more detailed analytical thinking, but increased anxiety under pressure. Tendency toward rumination and deeper processing.",
                "detail": "The Met allele produces a thermolabile enzyme with 3-4x lower activity. This increases prefrontal dopamine, enhancing cognitive function but potentially increasing stress vulnerability. Often called the 'Worrier' genotype."
            },
            "AG": {
                "effect": "Val/Met - Intermediate activity",
                "traits": "Balanced cognitive-emotional profile. Good cognitive flexibility with moderate stress resilience. Adaptive across varied situations.",
                "detail": "Heterozygotes show intermediate enzyme activity, often considered optimal for balancing cognitive performance with stress tolerance."
            },
            "GG": {
                "effect": "Val/Val - High COMT activity (Warrior)",
                "traits": "Lower prefrontal dopamine. Better performance under stress and pressure, improved emotional resilience, but may have lower baseline cognitive task performance. Action-oriented, less prone to overthinking.",
                "detail": "The Val allele produces highly active enzyme, rapidly clearing dopamine. This 'Warrior' genotype excels under pressure but may show reduced sustained attention and working memory at baseline."
            }
        },
        "interactions": ["rs6280", "rs1800497", "rs25531", "rs4633"],
        "references": ["Egan et al. 2001 PNAS", "Chen et al. 2004 Am J Hum Genet"]
    },

    "rs4633": {
        "gene": "COMT",
        "name": "COMT Haplotype Marker",
        "chromosome": "22",
        "function": "Additional COMT variant affecting enzyme expression",
        "category": "Dopamine System",
        "variants": {
            "CC": {
                "effect": "Higher COMT expression",
                "traits": "Supplements the Val158Met effect, potentially enhancing dopamine clearance.",
                "detail": "This variant can modify the overall COMT haplotype effect on dopamine metabolism."
            },
            "CT": {
                "effect": "Intermediate expression",
                "traits": "Moderate modification of COMT activity.",
                "detail": "Heterozygous state provides intermediate enzyme expression levels."
            },
            "TT": {
                "effect": "Lower COMT expression",
                "traits": "May enhance the effects of the Met allele at rs4680, further increasing prefrontal dopamine.",
                "detail": "Combined with Met/Met at rs4680, this may significantly increase dopamine availability."
            }
        },
        "interactions": ["rs4680"],
        "references": ["Meyer-Lindenberg et al. 2006"]
    },

    "rs1800497": {
        "gene": "DRD2/ANKK1",
        "name": "Taq1A Dopamine Receptor",
        "chromosome": "11",
        "function": "Affects D2 dopamine receptor density in striatum",
        "category": "Dopamine System",
        "variants": {
            "CC": {
                "effect": "Normal D2 receptor density (A2/A2)",
                "traits": "Standard reward sensitivity, typical motivation patterns, normal pleasure response.",
                "detail": "Normal D2 receptor availability supports standard dopaminergic reward signaling."
            },
            "CT": {
                "effect": "Reduced D2 receptors (A1/A2)",
                "traits": "Slightly enhanced novelty seeking, may need more stimulation for satisfaction, increased risk-taking tendency.",
                "detail": "30-40% reduced D2 receptor density may increase drive for rewarding stimuli."
            },
            "TT": {
                "effect": "Significantly reduced D2 receptors (A1/A1)",
                "traits": "Strong novelty seeking, reward deficiency patterns, higher sensation-seeking behavior, may seek intense experiences to achieve satisfaction.",
                "detail": "Substantially reduced D2 receptor availability (up to 40% lower) creates a 'reward deficiency' state, driving sensation-seeking behavior."
            }
        },
        "interactions": ["rs4680", "rs6280", "rs1079597"],
        "references": ["Blum et al. 1990", "Noble et al. 1991 Arch Gen Psychiatry"]
    },

    "rs6280": {
        "gene": "DRD3",
        "name": "Dopamine Receptor D3 Ser9Gly",
        "chromosome": "3",
        "function": "D3 receptor involved in reward and emotional processing",
        "category": "Dopamine System",
        "variants": {
            "CC": {
                "effect": "Ser/Ser - Standard receptor function",
                "traits": "Normal reward processing, typical emotional responses to rewards and punishments.",
                "detail": "Standard D3 receptor binding affinity supports normal mesolimbic dopamine signaling."
            },
            "CT": {
                "effect": "Ser/Gly - Intermediate",
                "traits": "Slightly modified reward sensitivity.",
                "detail": "Heterozygous state shows intermediate receptor binding characteristics."
            },
            "TT": {
                "effect": "Gly/Gly - Increased receptor affinity",
                "traits": "Enhanced emotional responses, potentially increased reward sensitivity, may show stronger motivation for pleasurable activities.",
                "detail": "The Gly variant shows higher dopamine binding affinity, potentially amplifying reward-related signals."
            }
        },
        "interactions": ["rs1800497", "rs4680"],
        "references": ["Lundstrom & Bhardwaj 2001", "Joyce et al. 2009"]
    },

    "rs1079597": {
        "gene": "DRD2",
        "name": "DRD2 TaqIB",
        "chromosome": "11",
        "function": "Additional D2 receptor density modifier",
        "category": "Dopamine System",
        "variants": {
            "CC": {
                "effect": "B1/B1 - Reduced D2 density",
                "traits": "Similar to A1 at rs1800497, associated with novelty seeking and reward sensitivity.",
                "detail": "Reduced receptor expression contributes to reward-seeking behavior patterns."
            },
            "CT": {
                "effect": "B1/B2 - Intermediate",
                "traits": "Moderate reward sensitivity.",
                "detail": "Heterozygous expression provides intermediate D2 availability."
            },
            "TT": {
                "effect": "B2/B2 - Normal D2 density",
                "traits": "Standard reward processing and satisfaction thresholds.",
                "detail": "Normal D2 receptor density supports typical reward signaling."
            }
        },
        "interactions": ["rs1800497"],
        "references": ["Noble et al. 1994"]
    },

    "rs1611115": {
        "gene": "DBH",
        "name": "Dopamine Beta-Hydroxylase",
        "chromosome": "9",
        "function": "Converts dopamine to norepinephrine",
        "category": "Dopamine System",
        "variants": {
            "CC": {
                "effect": "Higher DBH activity",
                "traits": "Efficient dopamine-to-norepinephrine conversion, balanced catecholamine levels.",
                "detail": "Normal enzyme activity maintains appropriate dopamine/norepinephrine ratios."
            },
            "CT": {
                "effect": "Intermediate activity",
                "traits": "Moderate catecholamine balance.",
                "detail": "Heterozygous state provides intermediate conversion efficiency."
            },
            "TT": {
                "effect": "Lower DBH activity",
                "traits": "Relatively higher dopamine, lower norepinephrine. May affect attention, arousal, and reward processing.",
                "detail": "Reduced DBH activity shifts catecholamine balance toward dopamine, potentially affecting cognitive and emotional processing."
            }
        },
        "interactions": ["rs4680", "rs6323"],
        "references": ["Zabetian et al. 2001"]
    },

    "rs27072": {
        "gene": "DAT1/SLC6A3",
        "name": "Dopamine Transporter",
        "chromosome": "5",
        "function": "Primary dopamine reuptake transporter",
        "category": "Dopamine System",
        "variants": {
            "CC": {
                "effect": "Standard transporter expression",
                "traits": "Normal dopamine clearance and signaling dynamics.",
                "detail": "Typical DAT1 expression supports normal dopaminergic transmission."
            },
            "CT": {
                "effect": "Intermediate expression",
                "traits": "Slightly modified dopamine signaling.",
                "detail": "Heterozygous state shows moderate transporter availability."
            },
            "TT": {
                "effect": "Altered transporter function",
                "traits": "Modified dopamine signaling dynamics, may affect attention and reward processing.",
                "detail": "Variant transporter function can alter dopamine availability in synapses."
            }
        },
        "interactions": ["rs4680", "rs1800497"],
        "references": ["Heinz et al. 2000"]
    },

    "rs2283265": {
        "gene": "DRD2",
        "name": "DRD2 Intronic Variant",
        "chromosome": "11",
        "function": "Affects D2 receptor alternative splicing",
        "category": "Dopamine System",
        "variants": {
            "GG": {
                "effect": "Standard splicing pattern",
                "traits": "Normal D2 short/long isoform ratio.",
                "detail": "Typical alternative splicing produces balanced receptor isoforms."
            },
            "GT": {
                "effect": "Intermediate splicing alteration",
                "traits": "Subtle changes in receptor isoform balance.",
                "detail": "Moderate effect on D2 receptor splice variant expression."
            },
            "TT": {
                "effect": "Altered D2S/D2L ratio",
                "traits": "Changed autoreceptor function, potentially affecting dopamine release regulation.",
                "detail": "Shift in D2 short (autoreceptor) vs long isoform ratio can modify dopamine feedback."
            }
        },
        "interactions": ["rs1800497"],
        "references": ["Zhang et al. 2007"]
    },

    # ============================================================================
    # MONOAMINE OXIDASE SYSTEM - Neurotransmitter breakdown
    # ============================================================================

    "rs6323": {
        "gene": "MAOA",
        "name": "Monoamine Oxidase A",
        "chromosome": "X",
        "function": "Degrades serotonin, dopamine, and norepinephrine",
        "category": "MAO System",
        "variants": {
            "TT": {
                "effect": "Higher MAO-A activity",
                "traits": "Faster neurotransmitter breakdown, generally calmer temperament, lower aggression propensity, more measured emotional responses.",
                "detail": "High MAO-A activity efficiently clears monoamines, associated with reduced impulsivity and aggression."
            },
            "GT": {
                "effect": "Intermediate activity (females only)",
                "traits": "Balanced neurotransmitter metabolism.",
                "detail": "Female heterozygotes show intermediate enzyme activity due to X-chromosome mosaicism."
            },
            "GG": {
                "effect": "Lower MAO-A activity",
                "traits": "Slower neurotransmitter breakdown, higher emotional intensity, potentially increased impulsivity. Strong environmental sensitivity - excellent outcomes in supportive environments, but increased risk of behavioral difficulties with adversity.",
                "detail": "Low MAO-A activity results in elevated monoamine levels, creating heightened emotional and behavioral reactivity. The 'Warrior Gene' designation reflects increased aggression potential, but this is highly environment-dependent."
            }
        },
        "interactions": ["rs4680", "rs25531"],
        "references": ["Caspi et al. 2002 Science", "Kim-Cohen et al. 2006"]
    },

    "rs1799836": {
        "gene": "MAOB",
        "name": "Monoamine Oxidase B",
        "chromosome": "X",
        "function": "Degrades dopamine and phenylethylamine",
        "category": "MAO System",
        "variants": {
            "AA": {
                "effect": "Standard activity",
                "traits": "Normal dopamine and trace amine metabolism.",
                "detail": "Typical MAO-B function supports baseline neurotransmitter clearance."
            },
            "AG": {
                "effect": "Intermediate (females)",
                "traits": "Moderate enzyme activity in heterozygous females.",
                "detail": "X-linked inheritance creates intermediate phenotype in females."
            },
            "GG": {
                "effect": "Altered activity",
                "traits": "Modified dopamine metabolism, may affect reward processing and personality traits.",
                "detail": "Variant MAO-B activity can influence dopaminergic tone and associated behaviors."
            }
        },
        "interactions": ["rs6323", "rs4680"],
        "references": ["Balciuniene et al. 2002"]
    },

    # ============================================================================
    # OXYTOCIN SYSTEM - Social bonding and trust
    # ============================================================================

    "rs53576": {
        "gene": "OXTR",
        "name": "Oxytocin Receptor",
        "chromosome": "3",
        "function": "Primary receptor for oxytocin social bonding hormone",
        "category": "Oxytocin System",
        "variants": {
            "AA": {
                "effect": "Reduced receptor expression",
                "traits": "Lower baseline empathy, reduced sensitivity to social cues, more self-reliant personality style, less affected by social rejection, may find solitude more comfortable.",
                "detail": "Reduced OXTR expression is associated with decreased oxytocin signaling, leading to lower sensitivity to social rewards and reduced distress from social isolation."
            },
            "AG": {
                "effect": "Intermediate expression",
                "traits": "Balanced social orientation with moderate empathy.",
                "detail": "Heterozygous individuals show intermediate social sensitivity and bonding tendencies."
            },
            "GG": {
                "effect": "Higher receptor expression",
                "traits": "Enhanced empathy, strong social orientation, higher sensitivity to social support and rejection, more attuned to others' emotions, tendency toward prosocial behavior.",
                "detail": "Increased OXTR expression amplifies oxytocin signaling, enhancing social reward sensitivity, empathy, and the importance of social connections."
            }
        },
        "interactions": ["rs2254298", "rs1042778"],
        "references": ["Rodrigues et al. 2009 PNAS", "Tost et al. 2010 PNAS"]
    },

    "rs2254298": {
        "gene": "OXTR",
        "name": "Oxytocin Receptor Variant 2",
        "chromosome": "3",
        "function": "Additional OXTR polymorphism affecting expression",
        "category": "Oxytocin System",
        "variants": {
            "AA": {
                "effect": "Lower expression variant",
                "traits": "Reduced social sensitivity, potentially more anxious attachment style.",
                "detail": "This variant has been associated with altered social processing and attachment behaviors."
            },
            "AG": {
                "effect": "Intermediate",
                "traits": "Moderate social processing characteristics.",
                "detail": "Balanced receptor expression supports typical social functioning."
            },
            "GG": {
                "effect": "Standard expression",
                "traits": "Typical social bonding capacity, normal empathy levels.",
                "detail": "Normal OXTR expression at this locus supports standard oxytocin signaling."
            }
        },
        "interactions": ["rs53576"],
        "references": ["Wu et al. 2012"]
    },

    "rs1042778": {
        "gene": "OXTR",
        "name": "Oxytocin Receptor 3'UTR",
        "chromosome": "3",
        "function": "Affects OXTR mRNA stability",
        "category": "Oxytocin System",
        "variants": {
            "GG": {
                "effect": "Standard mRNA stability",
                "traits": "Normal oxytocin receptor levels and social behavior patterns.",
                "detail": "Typical 3'UTR function maintains normal receptor expression."
            },
            "GT": {
                "effect": "Intermediate stability",
                "traits": "Slightly modified receptor expression.",
                "detail": "Heterozygous state shows moderate effect on mRNA half-life."
            },
            "TT": {
                "effect": "Altered mRNA stability",
                "traits": "May affect social behavior and prosociality.",
                "detail": "Modified 3'UTR sequence can influence receptor protein levels."
            }
        },
        "interactions": ["rs53576", "rs2254298"],
        "references": ["Israel et al. 2009"]
    },

    "rs3796863": {
        "gene": "CD38",
        "name": "CD38 ADP-ribosyl Cyclase",
        "chromosome": "4",
        "function": "Required for oxytocin release",
        "category": "Oxytocin System",
        "variants": {
            "AA": {
                "effect": "Reduced oxytocin release",
                "traits": "Lower social reward sensitivity, reduced parental attachment behaviors.",
                "detail": "Diminished CD38 function impairs calcium-dependent oxytocin secretion."
            },
            "AC": {
                "effect": "Intermediate",
                "traits": "Moderate oxytocin release capacity.",
                "detail": "Heterozygous state provides partial oxytocin release function."
            },
            "CC": {
                "effect": "Normal oxytocin release",
                "traits": "Typical social bonding, normal parental and pair bonding behaviors.",
                "detail": "Full CD38 activity supports normal oxytocin secretion and social behavior."
            }
        },
        "interactions": ["rs53576"],
        "references": ["Feldman et al. 2012"]
    },

    # ============================================================================
    # BDNF - Neuroplasticity and Learning
    # ============================================================================

    "rs6265": {
        "gene": "BDNF",
        "name": "Brain-Derived Neurotrophic Factor Val66Met",
        "chromosome": "11",
        "function": "Critical growth factor for neuron survival and plasticity",
        "category": "Neuroplasticity",
        "variants": {
            "AA": {
                "effect": "Met/Met - Reduced activity-dependent secretion",
                "traits": "Reduced hippocampal volume, potentially impaired episodic memory, higher anxiety, but may show enhanced habit learning. More resistant to changing established patterns.",
                "detail": "The Met variant impairs activity-dependent BDNF secretion by 25-30%, reducing synaptic plasticity. This affects memory formation and extinction but may enhance procedural learning."
            },
            "AG": {
                "effect": "Val/Met - Intermediate secretion",
                "traits": "Moderate balance between flexibility and stability in learning.",
                "detail": "Heterozygotes show intermediate BDNF secretion and neural plasticity characteristics."
            },
            "GG": {
                "effect": "Val/Val - Normal activity-dependent secretion",
                "traits": "Optimal hippocampal function, better episodic memory, enhanced fear extinction (ability to unlearn fear responses), more adaptable to new situations.",
                "detail": "Normal BDNF secretion supports robust synaptic plasticity, learning, and memory formation."
            }
        },
        "interactions": ["rs4680", "rs25531"],
        "references": ["Egan et al. 2003 Cell", "Hariri et al. 2003 J Neurosci"]
    },

    "rs7124442": {
        "gene": "BDNF",
        "name": "BDNF Regulatory Variant",
        "chromosome": "11",
        "function": "Affects BDNF transcription",
        "category": "Neuroplasticity",
        "variants": {
            "CC": {
                "effect": "Standard transcription",
                "traits": "Normal BDNF expression patterns.",
                "detail": "Typical regulatory function supports baseline neurotrophin production."
            },
            "CT": {
                "effect": "Intermediate",
                "traits": "Slightly modified BDNF levels.",
                "detail": "Heterozygous effect on transcriptional regulation."
            },
            "TT": {
                "effect": "Altered transcription",
                "traits": "May affect neuroplasticity and learning capacity.",
                "detail": "Modified transcription can influence BDNF protein availability."
            }
        },
        "interactions": ["rs6265"],
        "references": ["Verhagen et al. 2010"]
    },

    "rs11030104": {
        "gene": "BDNF",
        "name": "BDNF Intronic Variant",
        "chromosome": "11",
        "function": "Additional BDNF expression modifier",
        "category": "Neuroplasticity",
        "variants": {
            "AA": {
                "effect": "One variant state",
                "traits": "Modified BDNF expression patterns.",
                "detail": "This intronic variant can influence overall BDNF levels."
            },
            "AG": {
                "effect": "Intermediate",
                "traits": "Moderate effect on neurotrophin levels.",
                "detail": "Heterozygous state shows intermediate effects."
            },
            "GG": {
                "effect": "Alternative variant state",
                "traits": "Different BDNF expression profile.",
                "detail": "May modify the overall BDNF haplotype effect."
            }
        },
        "interactions": ["rs6265", "rs7124442"],
        "references": ["Verhagen et al. 2010"]
    },

    # ============================================================================
    # GABA SYSTEM - Inhibition and Anxiety
    # ============================================================================

    "rs211014": {
        "gene": "GABRA2",
        "name": "GABA-A Receptor Alpha-2",
        "chromosome": "4",
        "function": "Inhibitory neurotransmitter receptor",
        "category": "GABA System",
        "variants": {
            "CC": {
                "effect": "Standard receptor function",
                "traits": "Normal inhibitory tone, typical anxiety levels, standard stress responses.",
                "detail": "Normal GABA-A alpha-2 subunit expression supports balanced inhibition."
            },
            "CT": {
                "effect": "Intermediate",
                "traits": "Slightly modified GABAergic signaling.",
                "detail": "Heterozygous state shows moderate receptor function changes."
            },
            "TT": {
                "effect": "Altered receptor expression",
                "traits": "May have modified anxiety responses and stress reactivity.",
                "detail": "Variant receptor expression can affect inhibitory neurotransmission."
            }
        },
        "interactions": ["rs279858"],
        "references": ["Edenberg et al. 2004"]
    },

    "rs279858": {
        "gene": "GABRA2",
        "name": "GABA-A Receptor Alpha-2 Variant 2",
        "chromosome": "4",
        "function": "Additional GABRA2 polymorphism",
        "category": "GABA System",
        "variants": {
            "AA": {
                "effect": "One variant pattern",
                "traits": "Specific inhibitory signaling characteristics.",
                "detail": "Affects GABA-A receptor function and anxiety-related behaviors."
            },
            "AG": {
                "effect": "Intermediate",
                "traits": "Balanced inhibitory function.",
                "detail": "Heterozygous expression provides moderate effects."
            },
            "GG": {
                "effect": "Alternative pattern",
                "traits": "Different GABAergic signaling profile.",
                "detail": "May influence anxiety and stress response patterns."
            }
        },
        "interactions": ["rs211014"],
        "references": ["Covault et al. 2004"]
    },

    # ============================================================================
    # CIRCADIAN RHYTHM - Sleep and Chronotype
    # ============================================================================

    "rs57875989": {
        "gene": "PER2",
        "name": "Period Circadian Regulator 2",
        "chromosome": "2",
        "function": "Core circadian clock gene",
        "category": "Circadian",
        "variants": {
            "CC": {
                "effect": "Standard PER2 function",
                "traits": "Normal circadian rhythm, typical sleep-wake patterns.",
                "detail": "Normal PER2 activity maintains standard circadian periodicity."
            },
            "CG": {
                "effect": "Intermediate",
                "traits": "Slightly modified circadian timing.",
                "detail": "May show subtle differences in sleep timing preferences."
            },
            "GG": {
                "effect": "Altered circadian timing",
                "traits": "May have different chronotype (morning vs evening preference).",
                "detail": "Modified PER2 function can shift circadian phase."
            }
        },
        "interactions": ["rs1801260"],
        "references": ["Toh et al. 2001"]
    },

    "rs1801260": {
        "gene": "CLOCK",
        "name": "Circadian Locomotor Output Cycles Kaput",
        "chromosome": "4",
        "function": "Master circadian transcription factor",
        "category": "Circadian",
        "variants": {
            "AA": {
                "effect": "Standard CLOCK function",
                "traits": "Typical circadian rhythm, normal sleep patterns.",
                "detail": "Normal CLOCK activity drives standard circadian transcription."
            },
            "AG": {
                "effect": "Intermediate",
                "traits": "Slightly modified circadian characteristics.",
                "detail": "Heterozygous effect on circadian gene expression."
            },
            "GG": {
                "effect": "Evening chronotype tendency",
                "traits": "May prefer later sleep and wake times, potential 'night owl' tendency.",
                "detail": "This variant has been associated with delayed sleep phase and evening preference."
            }
        },
        "interactions": ["rs57875989"],
        "references": ["Katzenberg et al. 1998"]
    },

    "rs12649507": {
        "gene": "CLOCK",
        "name": "CLOCK Intronic Variant",
        "chromosome": "4",
        "function": "Additional circadian modifier",
        "category": "Circadian",
        "variants": {
            "AA": {
                "effect": "One chronotype pattern",
                "traits": "Influences morning vs evening preference.",
                "detail": "Contributes to overall chronotype phenotype."
            },
            "AG": {
                "effect": "Intermediate",
                "traits": "Moderate chronotype effects.",
                "detail": "Heterozygous influence on sleep timing."
            },
            "GG": {
                "effect": "Alternative chronotype pattern",
                "traits": "Different circadian timing preference.",
                "detail": "May shift toward morning or evening phenotype."
            }
        },
        "interactions": ["rs1801260"],
        "references": ["Jones et al. 2019 Nature Comms"]
    },

    # ============================================================================
    # STRESS RESPONSE - HPA Axis
    # ============================================================================

    "rs110402": {
        "gene": "CRHR1",
        "name": "Corticotropin Releasing Hormone Receptor 1",
        "chromosome": "17",
        "function": "Primary stress hormone receptor",
        "category": "Stress Response",
        "variants": {
            "AA": {
                "effect": "Reduced stress vulnerability",
                "traits": "Better stress resilience, less likely to develop anxiety or depression after trauma.",
                "detail": "This protective variant buffers against the psychological impact of stress."
            },
            "AG": {
                "effect": "Intermediate",
                "traits": "Moderate stress sensitivity.",
                "detail": "Balanced stress response characteristics."
            },
            "GG": {
                "effect": "Standard stress response",
                "traits": "Normal HPA axis reactivity, typical stress sensitivity.",
                "detail": "Standard CRHR1 function mediates typical stress responses."
            }
        },
        "interactions": ["rs242924"],
        "references": ["Bradley et al. 2008 Arch Gen Psychiatry"]
    },

    "rs242924": {
        "gene": "CRHR1",
        "name": "CRHR1 Intron 1",
        "chromosome": "17",
        "function": "Additional HPA axis modifier",
        "category": "Stress Response",
        "variants": {
            "GG": {
                "effect": "Protective variant",
                "traits": "Enhanced stress resilience.",
                "detail": "Provides additional protection against stress-related disorders."
            },
            "GT": {
                "effect": "Intermediate",
                "traits": "Moderate stress protection.",
                "detail": "Partial protective effect on stress outcomes."
            },
            "TT": {
                "effect": "Standard response",
                "traits": "Typical stress vulnerability.",
                "detail": "Normal HPA axis sensitivity to stress."
            }
        },
        "interactions": ["rs110402"],
        "references": ["Tyrka et al. 2009"]
    },

    "rs5522": {
        "gene": "NR3C2",
        "name": "Mineralocorticoid Receptor",
        "chromosome": "4",
        "function": "High-affinity cortisol receptor",
        "category": "Stress Response",
        "variants": {
            "AA": {
                "effect": "Ile variant - reduced function",
                "traits": "Higher cortisol reactivity, potentially more stress-sensitive.",
                "detail": "Reduced MR function impairs negative feedback on cortisol release."
            },
            "AG": {
                "effect": "Intermediate",
                "traits": "Moderate cortisol regulation.",
                "detail": "Balanced mineralocorticoid receptor activity."
            },
            "GG": {
                "effect": "Val variant - normal function",
                "traits": "Efficient cortisol regulation, better stress recovery.",
                "detail": "Normal MR function supports appropriate HPA axis feedback."
            }
        },
        "interactions": ["rs110402"],
        "references": ["DeRijk et al. 2006"]
    },

    "rs41423247": {
        "gene": "NR3C1",
        "name": "Glucocorticoid Receptor BclI",
        "chromosome": "5",
        "function": "Primary cortisol receptor",
        "category": "Stress Response",
        "variants": {
            "CC": {
                "effect": "Standard receptor sensitivity",
                "traits": "Normal cortisol responsiveness and HPA feedback.",
                "detail": "Typical glucocorticoid receptor function."
            },
            "CG": {
                "effect": "Increased sensitivity",
                "traits": "Enhanced cortisol sensitivity, may show stronger stress responses.",
                "detail": "Heterozygotes may have altered glucocorticoid signaling."
            },
            "GG": {
                "effect": "Highest sensitivity",
                "traits": "Strongly enhanced cortisol sensitivity, may be more affected by chronic stress.",
                "detail": "Increased GR sensitivity amplifies cortisol signaling effects."
            }
        },
        "interactions": ["rs5522", "rs110402"],
        "references": ["van Rossum et al. 2006"]
    },

    "rs1360780": {
        "gene": "FKBP5",
        "name": "FK506 Binding Protein 5",
        "chromosome": "6",
        "function": "Regulates glucocorticoid receptor sensitivity",
        "category": "Stress Response",
        "variants": {
            "CC": {
                "effect": "Standard FKBP5 expression",
                "traits": "Normal stress recovery, typical cortisol regulation.",
                "detail": "Normal FKBP5 levels provide appropriate GR modulation."
            },
            "CT": {
                "effect": "Intermediate expression",
                "traits": "Slightly altered stress response dynamics.",
                "detail": "Moderate effect on glucocorticoid receptor cycling."
            },
            "TT": {
                "effect": "Elevated FKBP5 expression",
                "traits": "Prolonged cortisol elevation after stress, slower stress recovery. Increased risk for stress-related disorders, but also potentially better threat detection.",
                "detail": "Higher FKBP5 impairs GR nuclear translocation, reducing negative feedback and prolonging stress responses."
            }
        },
        "interactions": ["rs41423247", "rs110402"],
        "references": ["Binder et al. 2008 JAMA"]
    },

    # ============================================================================
    # COGNITIVE TRAITS - Intelligence and Executive Function
    # ============================================================================

    "rs363050": {
        "gene": "SNAP25",
        "name": "Synaptosomal-Associated Protein 25",
        "chromosome": "20",
        "function": "Critical for neurotransmitter release",
        "category": "Cognition",
        "variants": {
            "AA": {
                "effect": "One variant",
                "traits": "Associated with different cognitive performance patterns.",
                "detail": "SNAP25 affects synaptic transmission efficiency."
            },
            "AG": {
                "effect": "Intermediate",
                "traits": "Moderate synaptic function characteristics.",
                "detail": "Balanced neurotransmitter release dynamics."
            },
            "GG": {
                "effect": "Alternative variant",
                "traits": "Different cognitive profile, has been associated with IQ variations.",
                "detail": "May affect attention and general cognitive ability."
            }
        },
        "interactions": ["rs4680"],
        "references": ["Gosso et al. 2006"]
    },

    "rs2760118": {
        "gene": "CHRM2",
        "name": "Muscarinic Acetylcholine Receptor M2",
        "chromosome": "7",
        "function": "Cholinergic receptor involved in cognition",
        "category": "Cognition",
        "variants": {
            "CC": {
                "effect": "Standard receptor function",
                "traits": "Normal cholinergic cognitive processing.",
                "detail": "Typical muscarinic receptor activity."
            },
            "CT": {
                "effect": "Intermediate",
                "traits": "Moderate cognitive effects.",
                "detail": "Balanced cholinergic signaling."
            },
            "TT": {
                "effect": "Altered receptor function",
                "traits": "Has been associated with IQ and cognitive performance differences.",
                "detail": "Modified cholinergic neurotransmission affecting cognition."
            }
        },
        "interactions": ["rs363050"],
        "references": ["Gosso et al. 2006"]
    },

    "rs17070145": {
        "gene": "WWC1/KIBRA",
        "name": "Kidney and Brain Expressed Protein",
        "chromosome": "5",
        "function": "Involved in memory consolidation",
        "category": "Cognition",
        "variants": {
            "CC": {
                "effect": "Lower memory performance",
                "traits": "Slightly reduced episodic memory capacity.",
                "detail": "This variant is associated with less efficient memory consolidation."
            },
            "CT": {
                "effect": "Intermediate memory",
                "traits": "Moderate memory performance.",
                "detail": "Balanced KIBRA function for memory processing."
            },
            "TT": {
                "effect": "Enhanced memory",
                "traits": "Better episodic memory, more efficient memory consolidation.",
                "detail": "This variant supports superior memory formation and retrieval."
            }
        },
        "interactions": ["rs6265"],
        "references": ["Papassotiropoulos et al. 2006 Science"]
    },

    # ============================================================================
    # IMPULSIVITY AND RISK-TAKING
    # ============================================================================

    "rs1800955": {
        "gene": "DRD4",
        "name": "Dopamine Receptor D4 Promoter",
        "chromosome": "11",
        "function": "D4 receptor affecting novelty seeking",
        "category": "Impulsivity",
        "variants": {
            "CC": {
                "effect": "Higher receptor expression",
                "traits": "Lower novelty seeking, more cautious approach to new experiences.",
                "detail": "Increased D4 receptor availability may reduce novelty-seeking drive."
            },
            "CT": {
                "effect": "Intermediate expression",
                "traits": "Balanced novelty seeking tendencies.",
                "detail": "Moderate D4 receptor levels."
            },
            "TT": {
                "effect": "Lower receptor expression",
                "traits": "Higher novelty seeking, more drawn to new and exciting experiences, greater risk tolerance.",
                "detail": "Reduced D4 expression associated with increased exploration and risk-taking."
            }
        },
        "interactions": ["rs1800497", "rs4680"],
        "references": ["Ebstein et al. 1996 Nature Genet", "Munafò et al. 2008"]
    },

    "rs7799039": {
        "gene": "LEP",
        "name": "Leptin",
        "chromosome": "7",
        "function": "Satiety hormone affecting reward",
        "category": "Impulsivity",
        "variants": {
            "AA": {
                "effect": "Lower leptin levels",
                "traits": "May have different reward sensitivity, potential impulsivity differences.",
                "detail": "Leptin interacts with dopamine reward circuits."
            },
            "AG": {
                "effect": "Intermediate",
                "traits": "Moderate leptin signaling.",
                "detail": "Balanced reward-satiety interaction."
            },
            "GG": {
                "effect": "Higher leptin levels",
                "traits": "Different reward processing characteristics.",
                "detail": "Higher baseline leptin may modify reward circuitry."
            }
        },
        "interactions": ["rs1800497"],
        "references": ["Kiefer et al. 2005"]
    },

    # ============================================================================
    # AGGRESSION AND EMOTIONAL REGULATION
    # ============================================================================

    "rs4714048": {
        "gene": "NTRK2",
        "name": "Neurotrophic Receptor Tyrosine Kinase 2",
        "chromosome": "9",
        "function": "BDNF receptor affecting emotional regulation",
        "category": "Emotion",
        "variants": {
            "AA": {
                "effect": "Standard receptor function",
                "traits": "Normal emotional regulation capacity.",
                "detail": "Typical TrkB receptor activity and BDNF signaling."
            },
            "AG": {
                "effect": "Intermediate",
                "traits": "Moderate emotional processing characteristics.",
                "detail": "Balanced neurotrophin signaling."
            },
            "GG": {
                "effect": "Altered receptor function",
                "traits": "May show different emotional regulation patterns.",
                "detail": "Modified BDNF-TrkB signaling can affect emotional processing."
            }
        },
        "interactions": ["rs6265"],
        "references": ["Smith et al. 2012"]
    },

    "rs1386483": {
        "gene": "NPSR1",
        "name": "Neuropeptide S Receptor 1",
        "chromosome": "7",
        "function": "Involved in anxiety and arousal",
        "category": "Emotion",
        "variants": {
            "AA": {
                "effect": "Standard receptor function",
                "traits": "Normal anxiety responses.",
                "detail": "Typical neuropeptide S signaling."
            },
            "AT": {
                "effect": "Intermediate",
                "traits": "Moderate anxiety characteristics.",
                "detail": "Balanced arousal and anxiety regulation."
            },
            "TT": {
                "effect": "Altered function",
                "traits": "May show modified anxiety and panic responses.",
                "detail": "Changed neuropeptide S signaling affecting anxiety circuits."
            }
        },
        "interactions": ["rs110402"],
        "references": ["Okamura et al. 2007"]
    },

    # ============================================================================
    # EMPATHY AND SOCIAL COGNITION
    # ============================================================================

    "rs6313": {
        "gene": "HTR2A",
        "name": "Serotonin Receptor 2A Promoter",
        "chromosome": "13",
        "function": "Affects 5-HT2A receptor expression",
        "category": "Social Cognition",
        "variants": {
            "CC": {
                "effect": "Lower receptor expression",
                "traits": "Potentially reduced emotional perception, different social cognition patterns.",
                "detail": "Reduced 5-HT2A may affect social-emotional processing."
            },
            "CT": {
                "effect": "Intermediate expression",
                "traits": "Balanced emotional perception.",
                "detail": "Moderate receptor levels for social cognition."
            },
            "TT": {
                "effect": "Higher receptor expression",
                "traits": "Enhanced emotional perception, possibly more empathic responses.",
                "detail": "Increased 5-HT2A availability may enhance emotional sensitivity."
            }
        },
        "interactions": ["rs53576", "rs6311"],
        "references": ["Spurlock et al. 1998"]
    },

    "rs2228485": {
        "gene": "AVPR1A",
        "name": "Arginine Vasopressin Receptor 1A",
        "chromosome": "12",
        "function": "Vasopressin receptor affecting social behavior",
        "category": "Social Cognition",
        "variants": {
            "CC": {
                "effect": "One variant pattern",
                "traits": "Influences pair bonding and social behavior.",
                "detail": "Affects vasopressin signaling in social circuits."
            },
            "CT": {
                "effect": "Intermediate",
                "traits": "Moderate social behavior characteristics.",
                "detail": "Balanced vasopressin receptor function."
            },
            "TT": {
                "effect": "Alternative pattern",
                "traits": "Different social attachment and bonding patterns.",
                "detail": "Modified vasopressin signaling affecting social behavior."
            }
        },
        "interactions": ["rs53576"],
        "references": ["Walum et al. 2008 PNAS"]
    },

    # ============================================================================
    # ADDICTION SUSCEPTIBILITY
    # ============================================================================

    "rs16969968": {
        "gene": "CHRNA5",
        "name": "Cholinergic Receptor Nicotinic Alpha 5",
        "chromosome": "15",
        "function": "Nicotinic receptor affecting addiction",
        "category": "Addiction",
        "variants": {
            "AA": {
                "effect": "Risk variant",
                "traits": "Higher nicotine dependence susceptibility if exposed.",
                "detail": "Altered receptor function affects nicotine reward and dependence."
            },
            "AG": {
                "effect": "Intermediate risk",
                "traits": "Moderate addiction susceptibility.",
                "detail": "Partial effect on nicotinic signaling."
            },
            "GG": {
                "effect": "Lower risk variant",
                "traits": "Lower nicotine dependence susceptibility.",
                "detail": "Normal receptor function with typical response to nicotine."
            }
        },
        "interactions": ["rs1800497"],
        "references": ["Thorgeirsson et al. 2008 Nature"]
    },

    "rs1229984": {
        "gene": "ADH1B",
        "name": "Alcohol Dehydrogenase 1B",
        "chromosome": "4",
        "function": "Primary alcohol metabolism enzyme",
        "category": "Addiction",
        "variants": {
            "CC": {
                "effect": "Fast metabolizer (His variant)",
                "traits": "Rapid alcohol metabolism leads to acetaldehyde accumulation, causing flushing and discomfort. Strong protection against alcohol dependence.",
                "detail": "The His variant metabolizes alcohol 40x faster, creating unpleasant effects that discourage heavy drinking."
            },
            "CT": {
                "effect": "Intermediate metabolism",
                "traits": "Partial protective effect against alcohol problems.",
                "detail": "Moderate alcohol metabolism rate."
            },
            "TT": {
                "effect": "Slow metabolizer (Arg variant)",
                "traits": "Standard alcohol metabolism without protective flushing response. Typical population risk for alcohol-related problems.",
                "detail": "Normal ADH1B activity without rapid acetaldehyde accumulation."
            }
        },
        "interactions": ["rs1800497", "rs671"],
        "references": ["Li et al. 2012 PLoS Med"]
    },

    "rs671": {
        "gene": "ALDH2",
        "name": "Aldehyde Dehydrogenase 2",
        "chromosome": "12",
        "function": "Acetaldehyde metabolism",
        "category": "Addiction",
        "variants": {
            "AA": {
                "effect": "Inactive enzyme (ALDH2*2/*2)",
                "traits": "Cannot process acetaldehyde. Severe flushing, nausea with any alcohol. Essentially complete protection against alcoholism, but increased esophageal cancer risk with drinking.",
                "detail": "Complete loss of ALDH2 activity causes toxic acetaldehyde accumulation with any alcohol consumption."
            },
            "AG": {
                "effect": "Reduced activity (ALDH2*1/*2)",
                "traits": "Partial flushing response, strong protection against alcohol dependence.",
                "detail": "Heterozygotes have ~50% reduced activity, causing unpleasant effects with drinking."
            },
            "GG": {
                "effect": "Normal enzyme (ALDH2*1/*1)",
                "traits": "Standard alcohol metabolism without flushing. Typical risk for alcohol-related problems.",
                "detail": "Full enzyme activity efficiently clears acetaldehyde."
            }
        },
        "interactions": ["rs1229984"],
        "references": ["Chen et al. 1999 Am J Hum Genet"]
    },

    # ============================================================================
    # OPENNESS AND CREATIVITY
    # ============================================================================

    "rs4633": {
        "gene": "COMT",
        "name": "COMT Synonymous Variant",
        "chromosome": "22",
        "function": "Linked to COMT activity haplotype",
        "category": "Creativity",
        "variants": {
            "CC": {
                "effect": "High activity haplotype marker",
                "traits": "Linked to faster dopamine clearance pattern.",
                "detail": "Part of COMT haplotype affecting prefrontal dopamine."
            },
            "CT": {
                "effect": "Intermediate",
                "traits": "Balanced COMT activity haplotype.",
                "detail": "Heterozygous haplotype effect."
            },
            "TT": {
                "effect": "Low activity haplotype marker",
                "traits": "Linked to higher prefrontal dopamine, potentially enhanced creativity and divergent thinking.",
                "detail": "Associated with increased prefrontal dopamine availability."
            }
        },
        "interactions": ["rs4680"],
        "references": ["Meyer-Lindenberg & Weinberger 2006"]
    },

    "rs4307059": {
        "gene": "DISC1",
        "name": "Disrupted in Schizophrenia 1",
        "chromosome": "1",
        "function": "Neurodevelopment and synaptic function",
        "category": "Creativity",
        "variants": {
            "CC": {
                "effect": "Standard function",
                "traits": "Typical cognitive patterns.",
                "detail": "Normal DISC1 function in neurodevelopment."
            },
            "CT": {
                "effect": "Intermediate",
                "traits": "Moderate effects on cognition.",
                "detail": "Partial variant effect."
            },
            "TT": {
                "effect": "Altered function",
                "traits": "Has been associated with divergent thinking and creative cognition.",
                "detail": "Modified DISC1 function may affect cognitive style."
            }
        },
        "interactions": ["rs4680", "rs6265"],
        "references": ["Kéri 2009 Psychol Sci"]
    },

    # ============================================================================
    # EXTRAVERSION AND SOCIABILITY
    # ============================================================================

    "rs2164273": {
        "gene": "SERT/SLC6A4",
        "name": "Serotonin Transporter Intron",
        "chromosome": "17",
        "function": "Additional serotonin transporter regulation",
        "category": "Extraversion",
        "variants": {
            "AA": {
                "effect": "One expression pattern",
                "traits": "Influences serotonin transport capacity.",
                "detail": "Contributes to overall serotonin transporter function."
            },
            "AG": {
                "effect": "Intermediate",
                "traits": "Balanced transporter characteristics.",
                "detail": "Heterozygous effect on transporter expression."
            },
            "GG": {
                "effect": "Alternative pattern",
                "traits": "Different serotonin signaling dynamics, may affect sociability.",
                "detail": "Modifies overall serotonin transporter phenotype."
            }
        },
        "interactions": ["rs25531"],
        "references": ["Wendland et al. 2006"]
    },

    # ============================================================================
    # CONSCIENTIOUSNESS AND PERSISTENCE
    # ============================================================================

    "rs4648317": {
        "gene": "DRD2",
        "name": "DRD2 Promoter",
        "chromosome": "11",
        "function": "D2 receptor expression regulation",
        "category": "Conscientiousness",
        "variants": {
            "AA": {
                "effect": "Standard promoter activity",
                "traits": "Normal D2 receptor levels and associated traits.",
                "detail": "Typical transcriptional regulation of DRD2."
            },
            "AG": {
                "effect": "Intermediate",
                "traits": "Moderate effect on receptor expression.",
                "detail": "Heterozygous influence on transcription."
            },
            "GG": {
                "effect": "Altered promoter activity",
                "traits": "Modified D2 expression, may affect persistence and goal-directed behavior.",
                "detail": "Changed transcriptional activity affecting receptor levels."
            }
        },
        "interactions": ["rs1800497"],
        "references": ["Zhang et al. 2007"]
    },

    # ============================================================================
    # NEUROTICISM AND NEGATIVE EMOTIONALITY
    # ============================================================================

    "rs3813034": {
        "gene": "SLC6A4",
        "name": "Serotonin Transporter 3'UTR",
        "chromosome": "17",
        "function": "Affects transporter mRNA stability",
        "category": "Neuroticism",
        "variants": {
            "GG": {
                "effect": "Standard mRNA stability",
                "traits": "Normal serotonin transporter levels.",
                "detail": "Typical 3'UTR function maintaining normal expression."
            },
            "GT": {
                "effect": "Intermediate stability",
                "traits": "Slightly modified transporter expression.",
                "detail": "Moderate effect on mRNA half-life."
            },
            "TT": {
                "effect": "Altered mRNA stability",
                "traits": "May affect neuroticism and negative emotionality.",
                "detail": "Modified 3'UTR sequence can influence transporter levels."
            }
        },
        "interactions": ["rs25531"],
        "references": ["Battersby et al. 1999"]
    },

    "rs7305115": {
        "gene": "TPH2",
        "name": "TPH2 Intronic Variant",
        "chromosome": "12",
        "function": "Serotonin synthesis modifier",
        "category": "Neuroticism",
        "variants": {
            "AA": {
                "effect": "Standard serotonin synthesis",
                "traits": "Normal emotional tone.",
                "detail": "Typical TPH2 expression and activity."
            },
            "AG": {
                "effect": "Intermediate",
                "traits": "Moderate synthesis levels.",
                "detail": "Balanced effect on serotonin production."
            },
            "GG": {
                "effect": "Modified synthesis",
                "traits": "May influence negative emotionality and neuroticism.",
                "detail": "Altered TPH2 function affecting central serotonin."
            }
        },
        "interactions": ["rs4570625", "rs25531"],
        "references": ["Gutknecht et al. 2007"]
    },

    # ============================================================================
    # RESILIENCE AND POSITIVE PSYCHOLOGY
    # ============================================================================

    "rs322931": {
        "gene": "AKT1",
        "name": "Protein Kinase B",
        "chromosome": "14",
        "function": "Survival signaling and neuroplasticity",
        "category": "Resilience",
        "variants": {
            "CC": {
                "effect": "Standard AKT signaling",
                "traits": "Normal cellular resilience and neuroplasticity.",
                "detail": "Typical AKT1 activity supporting cell survival."
            },
            "CT": {
                "effect": "Intermediate",
                "traits": "Moderate resilience characteristics.",
                "detail": "Balanced AKT signaling."
            },
            "TT": {
                "effect": "Altered signaling",
                "traits": "May affect stress resilience and adaptation capacity.",
                "detail": "Modified AKT activity influencing cellular responses."
            }
        },
        "interactions": ["rs6265", "rs4680"],
        "references": ["van Winkel et al. 2011"]
    },

    "rs165599": {
        "gene": "COMT",
        "name": "COMT 3'UTR",
        "chromosome": "22",
        "function": "COMT expression regulation",
        "category": "Resilience",
        "variants": {
            "AA": {
                "effect": "One expression pattern",
                "traits": "Influences overall COMT activity.",
                "detail": "3'UTR variant affecting mRNA stability."
            },
            "AG": {
                "effect": "Intermediate",
                "traits": "Balanced COMT expression.",
                "detail": "Moderate effect on enzyme levels."
            },
            "GG": {
                "effect": "Alternative pattern",
                "traits": "Different COMT expression, affecting dopamine metabolism.",
                "detail": "Modified post-transcriptional regulation."
            }
        },
        "interactions": ["rs4680"],
        "references": ["Meyer-Lindenberg et al. 2006"]
    },

    # ============================================================================
    # PAIN SENSITIVITY AND SENSORY PROCESSING
    # ============================================================================

    "rs1799971": {
        "gene": "OPRM1",
        "name": "Mu-Opioid Receptor A118G",
        "chromosome": "6",
        "function": "Primary endorphin/pain receptor",
        "category": "Pain",
        "variants": {
            "AA": {
                "effect": "Standard receptor function (Asn/Asn)",
                "traits": "Normal pain sensitivity, standard endorphin reward response, typical social bonding through opioid system.",
                "detail": "Normal mu-opioid receptor binding affinity and signaling."
            },
            "AG": {
                "effect": "Intermediate (Asn/Asp)",
                "traits": "Slightly reduced opioid binding, may have higher pain sensitivity.",
                "detail": "Reduced receptor function due to lower expression and binding."
            },
            "GG": {
                "effect": "Reduced receptor function (Asp/Asp)",
                "traits": "Higher pain sensitivity, may need more social connection for emotional comfort, reduced response to opioid reward. Higher resilience to opioid addiction.",
                "detail": "The G allele reduces receptor expression by 1.5-fold and binding affinity, altering pain and social reward processing."
            }
        },
        "interactions": ["rs53576"],
        "references": ["Way et al. 2009 Mol Psychiatry", "Fillingim et al. 2005"]
    },

    # ============================================================================
    # LONGEVITY-RELATED (May affect personality through life outlook)
    # ============================================================================

    "rs429358": {
        "gene": "APOE",
        "name": "Apolipoprotein E (defines E4)",
        "chromosome": "19",
        "function": "Lipid transport, brain health",
        "category": "Longevity",
        "variants": {
            "CC": {
                "effect": "E4 absent at this position",
                "traits": "Lower Alzheimer's risk, may affect long-term cognitive maintenance.",
                "detail": "Absence of the E4-defining variant is associated with better brain aging."
            },
            "CT": {
                "effect": "One E4 copy indicator",
                "traits": "Moderately elevated risk for late-onset cognitive decline.",
                "detail": "Heterozygous for E4-related variant."
            },
            "TT": {
                "effect": "E4/E4 indicator",
                "traits": "Highest risk for age-related cognitive decline.",
                "detail": "Homozygous for E4-associated variant."
            }
        },
        "interactions": ["rs7412"],
        "references": ["Corder et al. 1993 Science"]
    },

    "rs7412": {
        "gene": "APOE",
        "name": "Apolipoprotein E (defines E2)",
        "chromosome": "19",
        "function": "Additional APOE variant defining E2 allele",
        "category": "Longevity",
        "variants": {
            "CC": {
                "effect": "Not E2",
                "traits": "Standard APOE allele (E3 or E4 depending on rs429358).",
                "detail": "E3/E3 is most common and associated with average longevity."
            },
            "CT": {
                "effect": "One E2 copy",
                "traits": "E2 carriers may have enhanced longevity and cognitive protection.",
                "detail": "E2 is associated with better lipid metabolism and brain health."
            },
            "TT": {
                "effect": "E2/E2",
                "traits": "Potentially enhanced longevity but increased triglyceride levels.",
                "detail": "Homozygous E2 may confer exceptional longevity in some studies."
            }
        },
        "interactions": ["rs429358"],
        "references": ["Schächter et al. 1994"]
    }
}

# Gene interaction patterns for complex trait analysis
GENE_INTERACTIONS = {
    "stress_sensitivity": {
        "genes": ["rs25531", "rs4680", "rs6265", "rs110402", "rs1360780"],
        "description": "Stress response integration",
        "analysis": """
        The interaction between serotonin transporter (5-HTTLPR/rs25531), COMT (rs4680), BDNF (rs6265),
        and HPA axis genes (CRHR1, FKBP5) creates a complex stress response phenotype.

        Low-expression 5-HTTLPR + Met/Met COMT + Met/Met BDNF creates maximal stress sensitivity
        with deep emotional processing but vulnerability to chronic stress. This combination often
        appears in highly creative individuals who process emotions intensely.

        Conversely, high-expression 5-HTTLPR + Val/Val COMT + Val/Val BDNF creates a resilient,
        action-oriented phenotype that performs well under pressure but may miss subtle emotional cues.

        The CRHR1 and FKBP5 variants modify this foundation - protective CRHR1 variants can buffer
        an otherwise stress-sensitive genotype, while FKBP5 risk variants can compromise even
        a relatively resilient baseline.
        """
    },

    "reward_motivation": {
        "genes": ["rs4680", "rs1800497", "rs6280", "rs1800955", "rs6323"],
        "description": "Reward system integration",
        "analysis": """
        The dopamine system genes interact to create reward sensitivity and motivation profiles.

        Low COMT activity (Met/Met) + reduced D2 receptors (A1 carriers at rs1800497) + reduced D4
        expression (TT at rs1800955) creates a profile of high cognitive focus but potentially
        addictive reward-seeking behavior. These individuals may be driven, creative, but vulnerable
        to becoming over-focused on specific rewards.

        High COMT activity (Val/Val) + normal D2 (A2/A2) + normal D4 creates balanced reward
        processing with good stress tolerance but potentially lower intrinsic motivation for
        cognitive tasks.

        MAO-A activity (rs6323) modulates this system - low MAO-A increases emotional intensity
        and can amplify both reward highs and frustration lows.
        """
    },

    "social_bonding": {
        "genes": ["rs53576", "rs2254298", "rs3796863", "rs1799971", "rs2228485"],
        "description": "Social attachment system",
        "analysis": """
        The oxytocin-opioid social bonding network creates distinct attachment styles.

        GG genotype at OXTR (rs53576) + normal CD38 (rs3796863 CC) + standard mu-opioid receptor
        (rs1799971 AA) creates high social reward sensitivity, strong empathy, and deep need for
        social connection. These individuals thrive in supportive social environments but may
        be more affected by rejection.

        AA genotype at OXTR + reduced opioid function (rs1799971 GG) may create a more
        self-reliant personality that is less dependent on social validation but may also
        have to work harder to maintain close relationships.

        The vasopressin receptor (rs2228485) particularly influences pair bonding and can
        modify overall social attachment patterns.
        """
    },

    "cognitive_style": {
        "genes": ["rs4680", "rs6265", "rs17070145", "rs363050", "rs2760118"],
        "description": "Cognitive processing pattern",
        "analysis": """
        Cognitive style emerges from the interaction of prefrontal dopamine (COMT),
        neuroplasticity (BDNF), and memory consolidation (KIBRA) genes.

        Met/Met COMT + Val/Val BDNF + TT KIBRA (rs17070145) creates an optimal cognitive
        profile with high working memory, excellent episodic memory, and strong learning
        capacity. However, this combination may show performance decrements under high stress.

        Val/Val COMT + Met/Met BDNF creates a different pattern - better stress performance
        but potentially reduced baseline cognitive flexibility and memory consolidation.
        These individuals may excel at procedural learning and habit formation.

        SNAP25 (rs363050) and CHRM2 (rs2760118) variants can further modify general cognitive
        ability, affecting attention and processing speed.
        """
    },

    "emotional_temperament": {
        "genes": ["rs6295", "rs6311", "rs4570625", "rs211014", "rs6323"],
        "description": "Baseline emotional tone",
        "analysis": """
        Emotional temperament emerges from serotonin receptor balance, synthesis capacity,
        and GABAergic inhibition.

        Low 5-HT1A (rs6295 CC) + high 5-HT2A (rs6311 GG) + reduced TPH2 (rs4570625 TT)
        creates high emotional intensity - vivid emotions, strong aesthetic responses,
        but potential anxiety vulnerability.

        High 5-HT1A (rs6295 GG) + low 5-HT2A (rs6311 AA) + normal TPH2 creates a calmer,
        more emotionally stable temperament with lower anxiety but potentially reduced
        emotional richness.

        GABA receptor variants (rs211014) provide the inhibitory foundation that can
        buffer or amplify these serotonergic patterns. MAO-A activity (rs6323) affects
        how quickly emotional responses resolve.
        """
    },

    "creativity_openness": {
        "genes": ["rs4680", "rs6265", "rs4307059", "rs1800955", "rs6323"],
        "description": "Creative potential",
        "analysis": """
        Creative cognition involves a specific pattern of dopamine-BDNF interaction.

        The optimal 'creative genotype' often includes: Met/Met or Val/Met COMT (higher
        prefrontal dopamine), Val/Met or Val/Val BDNF (balanced plasticity), DRD4 variants
        associated with novelty seeking, and moderate MAO-A activity.

        This combination allows for divergent thinking (dopamine-enhanced prefrontal activity),
        cognitive flexibility (BDNF-mediated plasticity), novelty seeking (D4 receptor effects),
        and emotional intensity that fuels creative drive (moderate MAO-A).

        DISC1 variants (rs4307059) have been specifically linked to enhanced divergent thinking
        and creative achievement in multiple studies.
        """
    },

    "resilience_adversity": {
        "genes": ["rs110402", "rs242924", "rs1360780", "rs41423247", "rs6265"],
        "description": "Adversity response",
        "analysis": """
        Resilience to life adversity depends on HPA axis genetics interacting with neuroplasticity.

        Protective CRHR1 variants (rs110402 AA, rs242924 GG) + low-risk FKBP5 (rs1360780 CC) +
        Val/Val BDNF creates a resilient phenotype that recovers well from stress and shows
        effective fear extinction.

        Risk variants across these genes can create compound vulnerability - the individual
        may be strongly affected by early adversity, with effects that persist. However,
        this same sensitivity can lead to exceptional growth in supportive environments
        (differential susceptibility).

        The glucocorticoid receptor (rs41423247) modulates how cortisol affects the brain -
        high sensitivity variants amplify both the negative effects of chronic stress and
        the positive effects of nurturing environments.
        """
    },

    "circadian_energy": {
        "genes": ["rs1801260", "rs12649507", "rs57875989"],
        "description": "Daily rhythm and energy patterns",
        "analysis": """
        Circadian genes determine not just sleep timing but daily energy distribution
        and optimal performance windows.

        Evening-type variants (rs1801260 GG) create individuals who naturally peak later
        in the day, may struggle with early morning demands, but show enhanced creativity
        and problem-solving in evening hours.

        Morning-type variants support early rising, morning productivity, but earlier
        evening fatigue. These individuals may be perceived as more conscientious simply
        due to alignment with conventional schedules.

        PER2 variants (rs57875989) can shift the entire circadian phase, sometimes
        dramatically. Combined with CLOCK variants, this creates the full spectrum
        from extreme larks to extreme owls.
        """
    }
}

# Categories for organizing analysis
TRAIT_CATEGORIES = {
    "Serotonin System": "Mood regulation, emotional processing, and anxiety",
    "Dopamine System": "Reward, motivation, attention, and executive function",
    "MAO System": "Neurotransmitter metabolism and emotional intensity",
    "Oxytocin System": "Social bonding, empathy, and trust",
    "Neuroplasticity": "Learning, memory, and adaptation",
    "GABA System": "Inhibition, calmness, and anxiety regulation",
    "Circadian": "Sleep patterns and daily energy rhythms",
    "Stress Response": "HPA axis and stress resilience",
    "Cognition": "Intelligence and cognitive abilities",
    "Impulsivity": "Risk-taking and novelty seeking",
    "Emotion": "Emotional regulation and expression",
    "Social Cognition": "Understanding and relating to others",
    "Addiction": "Substance use susceptibility",
    "Creativity": "Divergent thinking and openness",
    "Extraversion": "Sociability and positive emotionality",
    "Conscientiousness": "Organization and persistence",
    "Neuroticism": "Negative emotionality and worry",
    "Resilience": "Stress recovery and positive adaptation",
    "Pain": "Sensory processing and pain sensitivity",
    "Longevity": "Cognitive aging and lifespan factors"
}
