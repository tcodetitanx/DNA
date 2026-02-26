# Comprehensive database of medical and physical trait SNPs
# Based on peer-reviewed genetic association studies and GWAS findings

MEDICAL_SNPS = {
    # ============================================================================
    # CARDIOVASCULAR HEALTH
    # ============================================================================

    "rs1333049": {
        "gene": "9p21.3",
        "name": "Coronary Artery Disease Risk Locus",
        "chromosome": "9",
        "function": "Major cardiovascular disease risk variant",
        "category": "Cardiovascular",
        "variants": {
            "CC": {
                "effect": "Higher risk variant",
                "traits": "Approximately 1.5-2x increased risk for coronary artery disease and heart attack. This is one of the strongest genetic risk factors for heart disease.",
                "detail": "The C allele is associated with increased atherosclerosis and plaque formation. This variant affects the CDKN2A/CDKN2B genes involved in cell cycle regulation and vascular smooth muscle proliferation."
            },
            "CG": {
                "effect": "Intermediate risk",
                "traits": "Moderately elevated cardiovascular risk, approximately 1.3x compared to baseline.",
                "detail": "Heterozygous individuals have intermediate risk between the two homozygous states."
            },
            "GG": {
                "effect": "Lower risk variant",
                "traits": "Population baseline risk for coronary artery disease.",
                "detail": "Standard cardiovascular risk profile at this locus."
            }
        },
        "implications": "Consider cardiovascular screening, maintain healthy lifestyle, monitor cholesterol and blood pressure",
        "references": ["McPherson et al. 2007 Science", "Helgadottir et al. 2007 Science"]
    },

    "rs10757278": {
        "gene": "9p21.3",
        "name": "CAD/MI Risk Variant",
        "chromosome": "9",
        "function": "Additional cardiovascular risk marker",
        "category": "Cardiovascular",
        "variants": {
            "AA": {
                "effect": "Protective",
                "traits": "Lower risk for coronary artery disease and myocardial infarction.",
                "detail": "Associated with reduced atherosclerotic burden."
            },
            "AG": {
                "effect": "Intermediate",
                "traits": "Moderate cardiovascular risk.",
                "detail": "Heterozygous risk profile."
            },
            "GG": {
                "effect": "Risk variant",
                "traits": "Elevated risk for heart disease, particularly in combination with other 9p21 variants.",
                "detail": "Increased susceptibility to coronary artery disease."
            }
        },
        "implications": "Cardiovascular risk assessment, lifestyle modifications recommended",
        "references": ["Samani et al. 2007 NEJM"]
    },

    "rs4977574": {
        "gene": "9p21.3",
        "name": "Third 9p21 Risk Variant",
        "chromosome": "9",
        "function": "Cardiovascular disease susceptibility",
        "category": "Cardiovascular",
        "variants": {
            "AA": {
                "effect": "Lower risk",
                "traits": "Reduced cardiovascular disease risk.",
                "detail": "Protective genotype for coronary artery disease."
            },
            "AG": {
                "effect": "Intermediate",
                "traits": "Moderate risk elevation.",
                "detail": "One copy of risk allele."
            },
            "GG": {
                "effect": "Higher risk",
                "traits": "Significantly elevated CAD risk, especially with other 9p21 risk variants.",
                "detail": "Combined with rs1333049 CC and rs10757278 GG creates multiplicative risk."
            }
        },
        "implications": "Part of the 9p21 risk haplotype assessment",
        "references": ["Schunkert et al. 2008"]
    },

    "rs1801133": {
        "gene": "MTHFR",
        "name": "C677T Methylenetetrahydrofolate Reductase",
        "chromosome": "1",
        "function": "Key enzyme in folate metabolism and homocysteine regulation",
        "category": "Cardiovascular",
        "variants": {
            "AA": {
                "effect": "Reduced enzyme activity (TT genotype)",
                "traits": "30-70% reduced MTHFR activity. Elevated homocysteine levels, increased cardiovascular risk if folate-deficient. May affect methylation processes throughout body.",
                "detail": "The thermolabile variant significantly reduces enzyme function, leading to elevated homocysteine which is a cardiovascular risk factor. Adequate folate, B12, and B6 intake can compensate for reduced enzyme activity."
            },
            "AG": {
                "effect": "Intermediate activity (CT genotype)",
                "traits": "Moderately reduced MTHFR activity, slightly elevated homocysteine risk.",
                "detail": "Heterozygotes have intermediate enzyme function and modest elevation of homocysteine."
            },
            "GG": {
                "effect": "Normal enzyme activity (CC genotype)",
                "traits": "Full MTHFR function, normal homocysteine metabolism.",
                "detail": "Standard folate cycle function."
            }
        },
        "implications": "Consider B-vitamin supplementation (folate, B12, B6), monitor homocysteine levels",
        "references": ["Frosst et al. 1995 Nature Genet"]
    },

    "rs1801131": {
        "gene": "MTHFR",
        "name": "A1298C MTHFR Variant",
        "chromosome": "1",
        "function": "Second common MTHFR polymorphism",
        "category": "Cardiovascular",
        "variants": {
            "GG": {
                "effect": "Reduced activity (CC genotype)",
                "traits": "Mild reduction in MTHFR activity, compound effect with rs1801133.",
                "detail": "Combined with C677T creates significantly reduced enzyme function."
            },
            "GT": {
                "effect": "Intermediate (AC genotype)",
                "traits": "Slight reduction in activity.",
                "detail": "Minor effect alone, more significant in compound heterozygotes."
            },
            "TT": {
                "effect": "Normal activity (AA genotype)",
                "traits": "Standard enzyme function at this position.",
                "detail": "Normal MTHFR activity contribution."
            }
        },
        "implications": "Assess in combination with C677T variant",
        "references": ["Weisberg et al. 1998"]
    },

    "rs662": {
        "gene": "PON1",
        "name": "Paraoxonase 1 Q192R",
        "chromosome": "7",
        "function": "Antioxidant enzyme protecting against LDL oxidation",
        "category": "Cardiovascular",
        "variants": {
            "AA": {
                "effect": "QQ genotype - Higher antioxidant activity",
                "traits": "Better protection against LDL oxidation, potentially reduced atherosclerosis risk.",
                "detail": "Q allele associated with greater high-density lipoprotein protective function."
            },
            "AG": {
                "effect": "QR genotype - Intermediate",
                "traits": "Moderate antioxidant protection.",
                "detail": "Intermediate HDL protective function."
            },
            "GG": {
                "effect": "RR genotype - Lower antioxidant activity for some substrates",
                "traits": "Different substrate specificity, may have higher cardiovascular risk in some populations.",
                "detail": "R allele has different enzymatic properties, overall cardiovascular impact depends on diet and exposures."
            }
        },
        "implications": "Antioxidant status, cardiovascular protection",
        "references": ["Mackness et al. 1997"]
    },

    "rs5082": {
        "gene": "APOA2",
        "name": "Apolipoprotein A-II",
        "chromosome": "1",
        "function": "HDL component affecting lipid metabolism",
        "category": "Cardiovascular",
        "variants": {
            "AA": {
                "effect": "Saturated fat sensitive",
                "traits": "Higher BMI and obesity risk when consuming high saturated fat diet. Normal weight on low saturated fat diet.",
                "detail": "This gene-diet interaction means saturated fat intake particularly affects weight in carriers of this variant."
            },
            "AG": {
                "effect": "Intermediate sensitivity",
                "traits": "Moderate response to dietary saturated fat.",
                "detail": "Some dietary fat sensitivity."
            },
            "GG": {
                "effect": "Less saturated fat sensitive",
                "traits": "Body weight less affected by saturated fat intake.",
                "detail": "More tolerant of higher saturated fat diets without weight gain."
            }
        },
        "implications": "Consider low saturated fat diet if AA genotype",
        "references": ["Corella et al. 2007 J Clin Invest"]
    },

    # ============================================================================
    # TYPE 2 DIABETES
    # ============================================================================

    "rs7903146": {
        "gene": "TCF7L2",
        "name": "Transcription Factor 7-Like 2",
        "chromosome": "10",
        "function": "Key diabetes risk gene affecting insulin secretion",
        "category": "Diabetes",
        "variants": {
            "CC": {
                "effect": "Lower diabetes risk",
                "traits": "Baseline population risk for type 2 diabetes. Normal beta cell function.",
                "detail": "Standard insulin secretion and glucose metabolism."
            },
            "CT": {
                "effect": "Intermediate risk",
                "traits": "1.4x increased risk for type 2 diabetes.",
                "detail": "Moderately impaired insulin secretion in response to glucose."
            },
            "TT": {
                "effect": "Highest diabetes risk",
                "traits": "Approximately 2x increased risk for type 2 diabetes. Impaired insulin secretion.",
                "detail": "This is the strongest common genetic risk factor for type 2 diabetes. Affects beta cell development and function, incretin signaling, and glucose-stimulated insulin release."
            }
        },
        "implications": "Diabetes screening recommended, weight management, glucose monitoring, consider low glycemic diet",
        "references": ["Grant et al. 2006 Nature Genet"]
    },

    "rs1801282": {
        "gene": "PPARG",
        "name": "Peroxisome Proliferator-Activated Receptor Gamma",
        "chromosome": "3",
        "function": "Master regulator of fat cell development and insulin sensitivity",
        "category": "Diabetes",
        "variants": {
            "CC": {
                "effect": "Pro/Pro - Normal risk",
                "traits": "Standard insulin sensitivity and diabetes risk.",
                "detail": "Normal PPARG function and adipocyte development."
            },
            "CG": {
                "effect": "Pro/Ala - Reduced risk",
                "traits": "15-25% reduced risk for type 2 diabetes. Better insulin sensitivity.",
                "detail": "The Ala variant improves insulin sensitivity and glucose metabolism."
            },
            "GG": {
                "effect": "Ala/Ala - Lowest risk",
                "traits": "Significantly reduced diabetes risk, enhanced insulin sensitivity.",
                "detail": "Homozygous protective genotype for metabolic health."
            }
        },
        "implications": "Favorable metabolic profile with G allele",
        "references": ["Altshuler et al. 2000 Nature Genet"]
    },

    "rs5219": {
        "gene": "KCNJ11",
        "name": "Potassium Channel J11 (E23K)",
        "chromosome": "11",
        "function": "Beta cell potassium channel affecting insulin secretion",
        "category": "Diabetes",
        "variants": {
            "CC": {
                "effect": "KK genotype - Higher risk",
                "traits": "Increased diabetes risk, reduced insulin secretion capacity.",
                "detail": "Altered potassium channel function impairs glucose-stimulated insulin release."
            },
            "CT": {
                "effect": "EK genotype - Intermediate",
                "traits": "Moderate diabetes risk elevation.",
                "detail": "Partial effect on insulin secretion."
            },
            "TT": {
                "effect": "EE genotype - Lower risk",
                "traits": "Normal insulin secretion, baseline diabetes risk.",
                "detail": "Standard potassium channel function."
            }
        },
        "implications": "Part of diabetes risk assessment",
        "references": ["Gloyn et al. 2003 Diabetes"]
    },

    "rs13266634": {
        "gene": "SLC30A8",
        "name": "Zinc Transporter 8",
        "chromosome": "8",
        "function": "Zinc transport in pancreatic beta cells",
        "category": "Diabetes",
        "variants": {
            "CC": {
                "effect": "Risk variant",
                "traits": "Elevated type 2 diabetes risk, reduced insulin secretion.",
                "detail": "Altered zinc homeostasis in beta cells affects insulin crystallization and secretion."
            },
            "CT": {
                "effect": "Intermediate",
                "traits": "Moderate diabetes risk.",
                "detail": "Partial effect on zinc transport and insulin processing."
            },
            "TT": {
                "effect": "Protective",
                "traits": "Lower diabetes risk, adequate zinc-mediated insulin processing.",
                "detail": "Normal beta cell zinc homeostasis."
            }
        },
        "implications": "Zinc status may be particularly important for beta cell function",
        "references": ["Sladek et al. 2007 Nature"]
    },

    "rs1111875": {
        "gene": "HHEX/IDE",
        "name": "Homeobox/Insulin Degrading Enzyme",
        "chromosome": "10",
        "function": "Beta cell development and insulin clearance",
        "category": "Diabetes",
        "variants": {
            "CC": {
                "effect": "Risk variant",
                "traits": "Increased diabetes risk.",
                "detail": "Affects pancreatic development and insulin degradation."
            },
            "CT": {
                "effect": "Intermediate",
                "traits": "Moderate risk elevation.",
                "detail": "Heterozygous effect."
            },
            "TT": {
                "effect": "Lower risk",
                "traits": "Baseline diabetes risk at this locus.",
                "detail": "Normal function."
            }
        },
        "implications": "Part of polygenic diabetes risk",
        "references": ["Saxena et al. 2007 Science"]
    },

    # ============================================================================
    # CANCER RISK
    # ============================================================================

    "rs1042522": {
        "gene": "TP53",
        "name": "p53 Arg72Pro",
        "chromosome": "17",
        "function": "Major tumor suppressor protein",
        "category": "Cancer",
        "variants": {
            "CC": {
                "effect": "Pro/Pro",
                "traits": "Associated with increased risk for certain cancers but potentially better survival. Different apoptosis efficiency.",
                "detail": "The Pro variant induces apoptosis less efficiently but may provide better cell cycle arrest, giving cells more time to repair DNA damage."
            },
            "CG": {
                "effect": "Arg/Pro",
                "traits": "Intermediate characteristics.",
                "detail": "Mixed p53 function."
            },
            "GG": {
                "effect": "Arg/Arg",
                "traits": "More efficient apoptosis induction, different cancer risk profile.",
                "detail": "The Arg variant is more efficient at inducing apoptosis. This may provide better cancer prevention but potentially worse outcomes if cancer develops."
            }
        },
        "implications": "Cancer risk awareness, appropriate screening",
        "references": ["Dumont et al. 2003 Nature Genet"]
    },

    "rs1799782": {
        "gene": "XRCC1",
        "name": "X-ray Repair Cross Complementing 1",
        "chromosome": "19",
        "function": "DNA repair enzyme",
        "category": "Cancer",
        "variants": {
            "CC": {
                "effect": "Arg/Arg - Normal repair",
                "traits": "Standard DNA repair capacity.",
                "detail": "Normal base excision repair function."
            },
            "CT": {
                "effect": "Arg/Trp - Reduced repair",
                "traits": "Mildly reduced DNA repair efficiency.",
                "detail": "Slight increase in sensitivity to DNA-damaging agents."
            },
            "TT": {
                "effect": "Trp/Trp - Further reduced repair",
                "traits": "Reduced DNA repair capacity, potentially higher sensitivity to carcinogens.",
                "detail": "Impaired base excision repair may increase cancer susceptibility, especially with environmental exposures."
            }
        },
        "implications": "Minimize carcinogen exposure, consider antioxidant support",
        "references": ["Lunn et al. 1999"]
    },

    "rs25487": {
        "gene": "XRCC1",
        "name": "XRCC1 Arg399Gln",
        "chromosome": "19",
        "function": "DNA repair scaffold protein",
        "category": "Cancer",
        "variants": {
            "GG": {
                "effect": "Arg/Arg - Normal",
                "traits": "Standard DNA repair.",
                "detail": "Normal scaffold function for base excision repair complex."
            },
            "AG": {
                "effect": "Arg/Gln - Intermediate",
                "traits": "Slightly reduced repair efficiency.",
                "detail": "Moderate effect on DNA repair capacity."
            },
            "AA": {
                "effect": "Gln/Gln - Reduced repair",
                "traits": "Reduced DNA repair efficiency, may have higher cancer risk with carcinogen exposure.",
                "detail": "Altered protein function reduces base excision repair effectiveness."
            }
        },
        "implications": "Avoid unnecessary radiation exposure, maintain antioxidant status",
        "references": ["Hu et al. 2005"]
    },

    "rs1800566": {
        "gene": "NQO1",
        "name": "NAD(P)H Quinone Dehydrogenase 1",
        "chromosome": "16",
        "function": "Detoxification enzyme protecting against oxidative stress",
        "category": "Cancer",
        "variants": {
            "CC": {
                "effect": "Normal enzyme activity",
                "traits": "Standard quinone detoxification, good protection against oxidative carcinogens.",
                "detail": "Full NQO1 enzyme function protecting cells from reactive oxygen species."
            },
            "CT": {
                "effect": "Intermediate activity",
                "traits": "Reduced but functional enzyme activity.",
                "detail": "Heterozygotes maintain some enzyme function."
            },
            "TT": {
                "effect": "No enzyme activity",
                "traits": "Complete loss of NQO1 function. Increased sensitivity to benzene and other quinone-forming carcinogens.",
                "detail": "The null phenotype significantly increases susceptibility to certain leukemias and may affect response to some chemotherapy drugs."
            }
        },
        "implications": "Avoid benzene exposure, may affect response to certain cancer treatments",
        "references": ["Ross et al. 2000"]
    },

    # ============================================================================
    # PHARMACOGENOMICS - Drug Metabolism
    # ============================================================================

    "rs1045642": {
        "gene": "ABCB1/MDR1",
        "name": "P-glycoprotein C3435T",
        "chromosome": "7",
        "function": "Drug efflux transporter affecting drug bioavailability",
        "category": "Pharmacogenomics",
        "variants": {
            "AA": {
                "effect": "TT genotype - Reduced P-gp expression",
                "traits": "Higher drug bioavailability for P-gp substrates, potentially more drug side effects but also better efficacy.",
                "detail": "Reduced drug efflux means more drug reaches target tissues. Affects many medications including immunosuppressants, HIV drugs, cancer drugs, and cardiac medications."
            },
            "AG": {
                "effect": "CT genotype - Intermediate",
                "traits": "Moderate P-glycoprotein function.",
                "detail": "Intermediate drug transport capacity."
            },
            "GG": {
                "effect": "CC genotype - Normal P-gp expression",
                "traits": "Standard drug efflux, typical drug dosing usually appropriate.",
                "detail": "Normal P-glycoprotein function maintaining typical drug levels."
            }
        },
        "implications": "May affect dosing of many medications, inform healthcare providers",
        "references": ["Hoffmeyer et al. 2000 PNAS"]
    },

    "rs1799853": {
        "gene": "CYP2C9",
        "name": "CYP2C9*2",
        "chromosome": "10",
        "function": "Major drug metabolizing enzyme",
        "category": "Pharmacogenomics",
        "variants": {
            "CC": {
                "effect": "Normal metabolizer (*1/*1)",
                "traits": "Standard metabolism of CYP2C9 substrates including warfarin, NSAIDs, and many other drugs.",
                "detail": "Normal enzyme activity allows standard drug dosing."
            },
            "CT": {
                "effect": "Intermediate metabolizer (*1/*2)",
                "traits": "Reduced metabolism, may need lower doses of affected medications.",
                "detail": "30-40% reduced enzyme activity."
            },
            "TT": {
                "effect": "Poor metabolizer (*2/*2)",
                "traits": "Significantly reduced drug metabolism. Higher risk for adverse effects with warfarin, require lower doses.",
                "detail": "Substantially reduced CYP2C9 activity, requires careful dose adjustment for affected medications."
            }
        },
        "implications": "Important for warfarin dosing, NSAID use, and many other medications",
        "references": ["Lee et al. 2002"]
    },

    "rs1057910": {
        "gene": "CYP2C9",
        "name": "CYP2C9*3",
        "chromosome": "10",
        "function": "Drug metabolizing enzyme variant",
        "category": "Pharmacogenomics",
        "variants": {
            "AA": {
                "effect": "Normal (*1/*1)",
                "traits": "Standard CYP2C9 function.",
                "detail": "Normal drug metabolism."
            },
            "AC": {
                "effect": "Intermediate (*1/*3)",
                "traits": "Reduced metabolism, lower drug doses may be needed.",
                "detail": "Approximately 70-80% reduced activity compared to wild type."
            },
            "CC": {
                "effect": "Poor metabolizer (*3/*3)",
                "traits": "Severely reduced drug metabolism, significantly lower warfarin doses required.",
                "detail": "Substantially impaired metabolism, high risk for adverse drug effects."
            }
        },
        "implications": "Critical for warfarin dosing and other CYP2C9 substrates",
        "references": ["Aithal et al. 1999"]
    },

    "rs9923231": {
        "gene": "VKORC1",
        "name": "Vitamin K Epoxide Reductase Complex 1",
        "chromosome": "16",
        "function": "Target of warfarin, vitamin K cycling",
        "category": "Pharmacogenomics",
        "variants": {
            "CC": {
                "effect": "Low sensitivity to warfarin",
                "traits": "Higher warfarin doses typically required (5-7 mg/day average).",
                "detail": "Higher VKORC1 expression means more enzyme to inhibit, requiring more warfarin."
            },
            "CT": {
                "effect": "Intermediate sensitivity",
                "traits": "Standard warfarin dosing range (4-5 mg/day average).",
                "detail": "Intermediate enzyme expression and warfarin sensitivity."
            },
            "TT": {
                "effect": "High sensitivity to warfarin",
                "traits": "Lower warfarin doses required (2-3 mg/day average). Higher bleeding risk if dose not adjusted.",
                "detail": "Reduced VKORC1 expression means less enzyme to inhibit, requiring less warfarin for therapeutic effect."
            }
        },
        "implications": "Critical for warfarin dosing - inform healthcare provider before starting anticoagulation",
        "references": ["Rieder et al. 2005 NEJM"]
    },

    "rs4244285": {
        "gene": "CYP2C19",
        "name": "CYP2C19*2",
        "chromosome": "10",
        "function": "Enzyme activating clopidogrel and metabolizing many drugs",
        "category": "Pharmacogenomics",
        "variants": {
            "GG": {
                "effect": "Normal metabolizer (*1/*1)",
                "traits": "Normal clopidogrel activation, standard response to proton pump inhibitors and other CYP2C19 substrates.",
                "detail": "Full enzyme function for drug metabolism."
            },
            "AG": {
                "effect": "Intermediate metabolizer (*1/*2)",
                "traits": "Reduced clopidogrel activation, may have reduced antiplatelet effect.",
                "detail": "One non-functional allele reduces overall enzyme capacity."
            },
            "AA": {
                "effect": "Poor metabolizer (*2/*2)",
                "traits": "Cannot activate clopidogrel effectively - may need alternative antiplatelet therapy. Different response to many medications.",
                "detail": "Loss of CYP2C19 function has significant implications for clopidogrel users and affects metabolism of many other drugs."
            }
        },
        "implications": "Critical for patients prescribed clopidogrel (Plavix) - alternative antiplatelet may be needed",
        "references": ["Mega et al. 2009 NEJM"]
    },

    "rs12248560": {
        "gene": "CYP2C19",
        "name": "CYP2C19*17",
        "chromosome": "10",
        "function": "Ultra-rapid metabolizer variant",
        "category": "Pharmacogenomics",
        "variants": {
            "CC": {
                "effect": "Normal metabolizer",
                "traits": "Standard CYP2C19 activity.",
                "detail": "Normal drug metabolism rate."
            },
            "CT": {
                "effect": "Increased activity (*1/*17)",
                "traits": "Enhanced drug metabolism, may need higher doses of some medications.",
                "detail": "Increased enzyme expression leads to faster drug clearance."
            },
            "TT": {
                "effect": "Ultra-rapid metabolizer (*17/*17)",
                "traits": "Very rapid drug metabolism. Enhanced clopidogrel response but may have reduced efficacy of medications that need to build up therapeutic levels.",
                "detail": "Significantly increased enzyme activity affecting many drug classes."
            }
        },
        "implications": "May need dose adjustments for various medications",
        "references": ["Sibbing et al. 2010"]
    },

    "rs1065852": {
        "gene": "CYP2D6",
        "name": "CYP2D6 Variant",
        "chromosome": "22",
        "function": "Major drug metabolizing enzyme affecting many medications",
        "category": "Pharmacogenomics",
        "variants": {
            "GG": {
                "effect": "Normal function",
                "traits": "Standard metabolism of CYP2D6 substrates including many antidepressants, beta blockers, opioids, and antipsychotics.",
                "detail": "Normal enzyme activity for extensive drug metabolism."
            },
            "AG": {
                "effect": "Intermediate",
                "traits": "Reduced metabolism of affected drugs.",
                "detail": "Partial reduction in enzyme function."
            },
            "AA": {
                "effect": "Reduced/poor function",
                "traits": "Significantly reduced CYP2D6 metabolism. May need dose adjustments for many common medications.",
                "detail": "Impaired metabolism of antidepressants (SSRIs, TCAs), codeine (won't convert to morphine), tamoxifen, and many other drugs."
            }
        },
        "implications": "Affects response to many medications - provide genotype info to healthcare providers",
        "references": ["Gaedigk et al. 2008"]
    },

    # ============================================================================
    # CAFFEINE AND NUTRITION
    # ============================================================================

    "rs762551": {
        "gene": "CYP1A2",
        "name": "Caffeine Metabolizer",
        "chromosome": "15",
        "function": "Primary enzyme for caffeine metabolism",
        "category": "Nutrition",
        "variants": {
            "AA": {
                "effect": "Fast caffeine metabolizer",
                "traits": "Rapid caffeine clearance, can consume coffee later in day without sleep disruption. May have cardiovascular benefit from moderate coffee consumption.",
                "detail": "High CYP1A2 activity clears caffeine quickly, reducing exposure time."
            },
            "AC": {
                "effect": "Intermediate metabolizer",
                "traits": "Moderate caffeine metabolism.",
                "detail": "Intermediate enzyme activity."
            },
            "CC": {
                "effect": "Slow caffeine metabolizer",
                "traits": "Caffeine persists longer, more likely to affect sleep. Higher cardiovascular risk from heavy coffee consumption.",
                "detail": "Reduced CYP1A2 activity means caffeine has prolonged effects. Studies show increased heart attack risk with heavy coffee consumption in slow metabolizers."
            }
        },
        "implications": "Slow metabolizers should limit coffee, especially avoid afternoon caffeine",
        "references": ["Cornelis et al. 2006 JAMA"]
    },

    "rs4988235": {
        "gene": "LCT/MCM6",
        "name": "Lactase Persistence",
        "chromosome": "2",
        "function": "Determines adult lactose digestion ability",
        "category": "Nutrition",
        "variants": {
            "GG": {
                "effect": "Lactose intolerant (ancestral)",
                "traits": "Lactase production declines after childhood. Difficulty digesting dairy products, may experience bloating, gas, and digestive discomfort.",
                "detail": "The ancestral state - lactase enzyme production decreases after weaning, making dairy digestion difficult."
            },
            "AG": {
                "effect": "Lactose tolerant (heterozygous)",
                "traits": "Can digest lactose into adulthood due to continued lactase production.",
                "detail": "One copy of the persistence allele is sufficient for lactose tolerance."
            },
            "AA": {
                "effect": "Lactose tolerant (homozygous)",
                "traits": "Full lactase persistence, easy dairy digestion throughout life.",
                "detail": "Continued lactase production throughout adulthood, common in populations with dairy-herding ancestry."
            }
        },
        "implications": "GG individuals should limit dairy or use lactase supplements",
        "references": ["Enattah et al. 2002 Nature Genet"]
    },

    "rs1801394": {
        "gene": "MTRR",
        "name": "Methionine Synthase Reductase",
        "chromosome": "5",
        "function": "Vitamin B12 metabolism and methylation",
        "category": "Nutrition",
        "variants": {
            "AA": {
                "effect": "Normal function",
                "traits": "Standard B12 metabolism and methylation.",
                "detail": "Normal methionine synthase reductase activity."
            },
            "AG": {
                "effect": "Intermediate",
                "traits": "Mildly reduced B12 metabolism efficiency.",
                "detail": "Moderate effect on methylation."
            },
            "GG": {
                "effect": "Reduced function",
                "traits": "Impaired B12 metabolism, may need higher B12 intake. Compounds with MTHFR variants.",
                "detail": "Reduced enzyme efficiency may require increased B12 supplementation, especially if also carrying MTHFR variants."
            }
        },
        "implications": "Consider B12 supplementation, especially combined with MTHFR variants",
        "references": ["Wilson et al. 1999"]
    },

    "rs1801198": {
        "gene": "TCN2",
        "name": "Transcobalamin II",
        "chromosome": "22",
        "function": "B12 transport protein",
        "category": "Nutrition",
        "variants": {
            "CC": {
                "effect": "Pro/Pro",
                "traits": "Higher holoTC levels, potentially less efficient B12 delivery to tissues.",
                "detail": "Different B12 transport dynamics."
            },
            "CG": {
                "effect": "Pro/Arg",
                "traits": "Intermediate B12 transport.",
                "detail": "Mixed transcobalamin function."
            },
            "GG": {
                "effect": "Arg/Arg",
                "traits": "Lower holoTC levels but potentially more efficient B12 delivery.",
                "detail": "Different B12 binding and release kinetics."
            }
        },
        "implications": "May affect interpretation of B12 tests and supplementation needs",
        "references": ["Miller et al. 2002"]
    },

    "rs7946": {
        "gene": "PEMT",
        "name": "Phosphatidylethanolamine N-Methyltransferase",
        "chromosome": "17",
        "function": "Choline synthesis pathway",
        "category": "Nutrition",
        "variants": {
            "CC": {
                "effect": "Higher choline requirement",
                "traits": "Reduced endogenous choline synthesis, higher dietary choline needs. May be more susceptible to fatty liver on low choline diet.",
                "detail": "The C allele reduces PEMT activity, increasing reliance on dietary choline."
            },
            "CT": {
                "effect": "Intermediate",
                "traits": "Moderate choline synthesis capacity.",
                "detail": "Partial effect on choline production."
            },
            "TT": {
                "effect": "Normal choline synthesis",
                "traits": "Adequate endogenous choline production.",
                "detail": "Full PEMT activity for choline synthesis."
            }
        },
        "implications": "CC carriers should ensure adequate dietary choline (eggs, liver, etc.)",
        "references": ["da Costa et al. 2006"]
    },

    # ============================================================================
    # OBESITY AND METABOLISM
    # ============================================================================

    "rs9939609": {
        "gene": "FTO",
        "name": "Fat Mass and Obesity Associated",
        "chromosome": "16",
        "function": "Energy balance and adipogenesis regulation",
        "category": "Metabolism",
        "variants": {
            "TT": {
                "effect": "Lower obesity risk",
                "traits": "Baseline obesity risk, normal appetite regulation.",
                "detail": "Standard FTO function."
            },
            "AT": {
                "effect": "Intermediate risk",
                "traits": "1.3x increased obesity risk, slightly increased caloric intake.",
                "detail": "One copy of risk allele moderately affects body weight."
            },
            "AA": {
                "effect": "Higher obesity risk",
                "traits": "1.7x increased obesity risk. Tendency toward increased food intake, preference for high-calorie foods. Can be overcome with physical activity and dietary awareness.",
                "detail": "The A allele affects hypothalamic appetite regulation, increasing food intake and body weight. However, physical activity can negate this genetic risk."
            }
        },
        "implications": "AA carriers particularly benefit from regular exercise and mindful eating",
        "references": ["Frayling et al. 2007 Science"]
    },

    "rs17782313": {
        "gene": "MC4R",
        "name": "Melanocortin 4 Receptor",
        "chromosome": "18",
        "function": "Appetite and energy homeostasis",
        "category": "Metabolism",
        "variants": {
            "TT": {
                "effect": "Lower obesity risk",
                "traits": "Normal appetite regulation.",
                "detail": "Standard MC4R signaling."
            },
            "CT": {
                "effect": "Intermediate",
                "traits": "Moderately increased obesity risk.",
                "detail": "Partial effect on satiety signaling."
            },
            "CC": {
                "effect": "Higher obesity risk",
                "traits": "Increased appetite, reduced satiety signaling, higher obesity risk.",
                "detail": "Impaired melanocortin signaling affects hunger and fullness cues."
            }
        },
        "implications": "Focus on satiety-promoting foods (protein, fiber) and mindful eating",
        "references": ["Loos et al. 2008 Nature Genet"]
    },

    "rs1558902": {
        "gene": "FTO",
        "name": "FTO Intron 1 Variant",
        "chromosome": "16",
        "function": "Additional obesity-associated variant",
        "category": "Metabolism",
        "variants": {
            "TT": {
                "effect": "Lower risk",
                "traits": "Reduced obesity susceptibility.",
                "detail": "Protective pattern at this FTO locus."
            },
            "AT": {
                "effect": "Intermediate",
                "traits": "Moderate obesity risk.",
                "detail": "One risk allele present."
            },
            "AA": {
                "effect": "Higher risk",
                "traits": "Elevated obesity risk, particularly in sedentary individuals.",
                "detail": "Strong effect on body mass, mitigated by physical activity."
            }
        },
        "implications": "Physical activity particularly important for risk allele carriers",
        "references": ["Speliotes et al. 2010 Nature Genet"]
    },

    # ============================================================================
    # AUTOIMMUNE CONDITIONS
    # ============================================================================

    "rs2476601": {
        "gene": "PTPN22",
        "name": "Protein Tyrosine Phosphatase Non-Receptor 22",
        "chromosome": "1",
        "function": "T-cell signaling regulation",
        "category": "Autoimmune",
        "variants": {
            "GG": {
                "effect": "Normal T-cell signaling",
                "traits": "Baseline autoimmune risk.",
                "detail": "Standard PTPN22 function in immune regulation."
            },
            "AG": {
                "effect": "One risk allele",
                "traits": "Increased risk for multiple autoimmune conditions including rheumatoid arthritis, type 1 diabetes, lupus, and thyroid disease.",
                "detail": "The risk allele creates a gain-of-function variant that alters T-cell signaling."
            },
            "AA": {
                "effect": "Two risk alleles",
                "traits": "Significantly elevated autoimmune risk.",
                "detail": "Strongly altered immune regulation increasing susceptibility to autoimmune conditions."
            }
        },
        "implications": "Be aware of autoimmune condition symptoms, early detection important",
        "references": ["Bottini et al. 2004 Nature Genet"]
    },

    "rs3087243": {
        "gene": "CTLA4",
        "name": "Cytotoxic T-Lymphocyte Associated Protein 4",
        "chromosome": "2",
        "function": "Immune checkpoint, prevents autoimmunity",
        "category": "Autoimmune",
        "variants": {
            "AA": {
                "effect": "Lower CTLA4 expression",
                "traits": "Increased risk for autoimmune thyroid disease, type 1 diabetes, and other autoimmune conditions.",
                "detail": "Reduced immune checkpoint function may allow inappropriate immune responses."
            },
            "AG": {
                "effect": "Intermediate",
                "traits": "Moderate autoimmune risk.",
                "detail": "Intermediate CTLA4 expression."
            },
            "GG": {
                "effect": "Normal expression",
                "traits": "Baseline autoimmune risk.",
                "detail": "Standard immune checkpoint function."
            }
        },
        "implications": "Monitor for thyroid and other autoimmune conditions",
        "references": ["Ueda et al. 2003 Nature"]
    },

    "rs2104286": {
        "gene": "IL2RA",
        "name": "Interleukin 2 Receptor Alpha",
        "chromosome": "10",
        "function": "T-cell activation and regulation",
        "category": "Autoimmune",
        "variants": {
            "AA": {
                "effect": "Risk variant",
                "traits": "Increased risk for multiple sclerosis and type 1 diabetes.",
                "detail": "Altered IL-2 receptor signaling affects regulatory T-cell function."
            },
            "AG": {
                "effect": "Intermediate",
                "traits": "Moderate risk elevation.",
                "detail": "Heterozygous effect."
            },
            "GG": {
                "effect": "Protective",
                "traits": "Reduced risk for these autoimmune conditions.",
                "detail": "Normal IL-2 receptor alpha chain expression."
            }
        },
        "implications": "Part of autoimmune risk assessment",
        "references": ["Hafler et al. 2007 NEJM"]
    },

    # ============================================================================
    # BONE HEALTH
    # ============================================================================

    "rs2282679": {
        "gene": "GC/DBP",
        "name": "Vitamin D Binding Protein",
        "chromosome": "4",
        "function": "Vitamin D transport and bioavailability",
        "category": "Bone Health",
        "variants": {
            "TT": {
                "effect": "Higher vitamin D levels",
                "traits": "Better vitamin D status, improved bone health potential.",
                "detail": "Higher circulating 25(OH)D levels with same sun exposure or supplementation."
            },
            "GT": {
                "effect": "Intermediate",
                "traits": "Moderate vitamin D levels.",
                "detail": "Intermediate transport capacity."
            },
            "GG": {
                "effect": "Lower vitamin D levels",
                "traits": "Lower circulating vitamin D despite similar exposure. May need higher supplementation.",
                "detail": "Reduced vitamin D binding protein function affects circulating levels."
            }
        },
        "implications": "GG carriers may need higher vitamin D supplementation",
        "references": ["Wang et al. 2010 Lancet"]
    },

    "rs2228570": {
        "gene": "VDR",
        "name": "Vitamin D Receptor FokI",
        "chromosome": "12",
        "function": "Vitamin D receptor affecting calcium and bone metabolism",
        "category": "Bone Health",
        "variants": {
            "GG": {
                "effect": "FF genotype - More active receptor",
                "traits": "Potentially better bone mineral density with adequate vitamin D.",
                "detail": "Shorter, more active VDR protein."
            },
            "AG": {
                "effect": "Ff - Intermediate",
                "traits": "Moderate receptor activity.",
                "detail": "Mixed VDR function."
            },
            "AA": {
                "effect": "ff - Less active receptor",
                "traits": "May need higher vitamin D for optimal bone health.",
                "detail": "Longer VDR protein with reduced transcriptional activity."
            }
        },
        "implications": "Ensure adequate vitamin D intake, especially AA carriers",
        "references": ["Fang et al. 2005"]
    },

    "rs1544410": {
        "gene": "VDR",
        "name": "VDR BsmI",
        "chromosome": "12",
        "function": "Vitamin D receptor variant",
        "category": "Bone Health",
        "variants": {
            "CC": {
                "effect": "bb genotype",
                "traits": "Different bone metabolism characteristics.",
                "detail": "Associated with vitamin D metabolism differences."
            },
            "CT": {
                "effect": "Bb genotype",
                "traits": "Intermediate VDR function.",
                "detail": "Heterozygous effect."
            },
            "TT": {
                "effect": "BB genotype",
                "traits": "Alternative VDR expression pattern.",
                "detail": "May affect calcium absorption and bone density."
            }
        },
        "implications": "Part of comprehensive VDR assessment",
        "references": ["Morrison et al. 1994 Nature"]
    },

    # ============================================================================
    # INFLAMMATION
    # ============================================================================

    "rs1800795": {
        "gene": "IL6",
        "name": "Interleukin-6 Promoter",
        "chromosome": "7",
        "function": "Major inflammatory cytokine",
        "category": "Inflammation",
        "variants": {
            "GG": {
                "effect": "Higher IL-6 production",
                "traits": "Increased inflammatory response, may have higher CRP levels, potentially higher risk for inflammatory conditions.",
                "detail": "Higher baseline IL-6 expression creates a more pro-inflammatory state."
            },
            "GC": {
                "effect": "Intermediate",
                "traits": "Moderate inflammatory response.",
                "detail": "Intermediate IL-6 production."
            },
            "CC": {
                "effect": "Lower IL-6 production",
                "traits": "Reduced baseline inflammation, potentially better metabolic health.",
                "detail": "Lower constitutive IL-6 may reduce chronic inflammation risk."
            }
        },
        "implications": "Anti-inflammatory diet and lifestyle particularly important for GG carriers",
        "references": ["Fishman et al. 1998"]
    },

    "rs1800629": {
        "gene": "TNF",
        "name": "Tumor Necrosis Factor Alpha Promoter",
        "chromosome": "6",
        "function": "Major pro-inflammatory cytokine",
        "category": "Inflammation",
        "variants": {
            "GG": {
                "effect": "Normal TNF production",
                "traits": "Standard inflammatory response.",
                "detail": "Baseline TNF-alpha expression."
            },
            "AG": {
                "effect": "Increased TNF production",
                "traits": "Enhanced inflammatory response, may affect response to infections and autoimmune conditions.",
                "detail": "Higher TNF-alpha expression."
            },
            "AA": {
                "effect": "Highest TNF production",
                "traits": "Significantly elevated inflammatory potential, increased risk for certain inflammatory conditions.",
                "detail": "Strongly enhanced TNF-alpha transcription."
            }
        },
        "implications": "Anti-inflammatory lifestyle important, may respond well to TNF-targeted therapies",
        "references": ["Wilson et al. 1997"]
    },

    "rs1205": {
        "gene": "CRP",
        "name": "C-Reactive Protein",
        "chromosome": "1",
        "function": "Acute phase inflammatory marker",
        "category": "Inflammation",
        "variants": {
            "CC": {
                "effect": "Higher baseline CRP",
                "traits": "Tends toward higher circulating CRP levels, may show elevated inflammation markers.",
                "detail": "Genetic tendency toward higher inflammatory marker production."
            },
            "CT": {
                "effect": "Intermediate",
                "traits": "Moderate baseline CRP levels.",
                "detail": "Intermediate inflammatory marker expression."
            },
            "TT": {
                "effect": "Lower baseline CRP",
                "traits": "Tends toward lower inflammation markers.",
                "detail": "Reduced baseline CRP production."
            }
        },
        "implications": "Consider genetic component when interpreting CRP test results",
        "references": ["Crawford et al. 2006"]
    },

    # ============================================================================
    # BLOOD CLOTTING
    # ============================================================================

    "rs6025": {
        "gene": "F5",
        "name": "Factor V Leiden",
        "chromosome": "1",
        "function": "Blood clotting factor",
        "category": "Clotting",
        "variants": {
            "CC": {
                "effect": "Homozygous Factor V Leiden",
                "traits": "80x increased risk for venous thromboembolism (blood clots). Requires medical management and awareness.",
                "detail": "Severely impaired protein C anticoagulant pathway. Significant thrombophilia requiring medical attention."
            },
            "CT": {
                "effect": "Heterozygous Factor V Leiden",
                "traits": "5-7x increased risk for venous blood clots. Should avoid additional risk factors (smoking, oral contraceptives, immobility).",
                "detail": "Partially impaired anticoagulant function. Most common inherited thrombophilia."
            },
            "TT": {
                "effect": "Normal",
                "traits": "No Factor V Leiden mutation, baseline clotting risk.",
                "detail": "Normal protein C anticoagulant pathway."
            }
        },
        "implications": "CRITICAL: Carriers should inform healthcare providers. Avoid estrogen-based contraceptives, maintain mobility during travel, prevent dehydration",
        "references": ["Bertina et al. 1994 Nature"]
    },

    "rs1799963": {
        "gene": "F2",
        "name": "Prothrombin G20210A",
        "chromosome": "11",
        "function": "Prothrombin (Factor II) production",
        "category": "Clotting",
        "variants": {
            "GG": {
                "effect": "Normal",
                "traits": "Baseline clotting function.",
                "detail": "Normal prothrombin levels."
            },
            "AG": {
                "effect": "Heterozygous carrier",
                "traits": "2-3x increased risk for venous thromboembolism. Elevated prothrombin levels.",
                "detail": "Increased prothrombin production creates hypercoagulable state."
            },
            "AA": {
                "effect": "Homozygous (rare)",
                "traits": "Significantly elevated clotting risk.",
                "detail": "Substantially increased prothrombin and thrombosis risk."
            }
        },
        "implications": "Carriers should inform healthcare providers about thrombophilia, avoid additional risk factors",
        "references": ["Poort et al. 1996 Blood"]
    },

    "rs5985": {
        "gene": "F13A1",
        "name": "Factor XIII Val34Leu",
        "chromosome": "6",
        "function": "Clot stabilization",
        "category": "Clotting",
        "variants": {
            "CC": {
                "effect": "Val/Val - Normal clot structure",
                "traits": "Standard clot formation and stability.",
                "detail": "Normal fibrin crosslinking."
            },
            "CT": {
                "effect": "Val/Leu - Modified clot structure",
                "traits": "Altered clot structure, may be protective against thrombosis.",
                "detail": "Modified Factor XIII activity creating different clot architecture."
            },
            "TT": {
                "effect": "Leu/Leu - Different clot formation",
                "traits": "May have some protection against thrombotic events but different bleeding characteristics.",
                "detail": "Significantly altered fibrin crosslinking affecting clot stability."
            }
        },
        "implications": "May affect surgical bleeding and clot characteristics",
        "references": ["Ariens et al. 2002"]
    },

    # ============================================================================
    # VISION AND HEARING
    # ============================================================================

    "rs10034228": {
        "gene": "LOXL1",
        "name": "Lysyl Oxidase-Like 1",
        "chromosome": "15",
        "function": "Extracellular matrix maintenance",
        "category": "Vision",
        "variants": {
            "CC": {
                "effect": "Higher exfoliation glaucoma risk",
                "traits": "Significantly increased risk for exfoliation syndrome and exfoliation glaucoma.",
                "detail": "Altered elastic fiber formation in eye tissues."
            },
            "CT": {
                "effect": "Intermediate",
                "traits": "Moderately elevated glaucoma risk.",
                "detail": "One risk allele present."
            },
            "TT": {
                "effect": "Lower risk",
                "traits": "Reduced risk for exfoliation glaucoma.",
                "detail": "Normal elastic fiber metabolism."
            }
        },
        "implications": "Regular eye exams important, especially for CC carriers",
        "references": ["Thorleifsson et al. 2007 Science"]
    },

    "rs1800407": {
        "gene": "OCA2",
        "name": "Oculocutaneous Albinism II",
        "chromosome": "15",
        "function": "Melanin production affecting eye color",
        "category": "Vision",
        "variants": {
            "GG": {
                "effect": "Brown eye tendency",
                "traits": "Higher melanin production in iris, brown eye color more likely.",
                "detail": "Standard OCA2 function supporting melanin synthesis."
            },
            "AG": {
                "effect": "Intermediate",
                "traits": "Variable eye color, often green or hazel.",
                "detail": "Moderate melanin production."
            },
            "AA": {
                "effect": "Blue eye tendency",
                "traits": "Reduced iris melanin, blue or light eye color more likely.",
                "detail": "Reduced OCA2 activity decreases iris pigmentation."
            }
        },
        "implications": "Light eye color may mean more UV sensitivity - wear sunglasses",
        "references": ["Duffy et al. 2007 AJHG"]
    },

    "rs12913832": {
        "gene": "HERC2/OCA2",
        "name": "Eye Color Determinant",
        "chromosome": "15",
        "function": "Major eye color gene regulatory element",
        "category": "Vision",
        "variants": {
            "AA": {
                "effect": "Brown eyes (dominant)",
                "traits": "Brown eye color, higher iris melanin.",
                "detail": "Enhancer active, full OCA2 expression in iris."
            },
            "AG": {
                "effect": "Variable (usually brown or green)",
                "traits": "Mixed eye color, often brown, hazel, or green.",
                "detail": "Intermediate OCA2 expression."
            },
            "GG": {
                "effect": "Blue eyes",
                "traits": "Blue eye color due to minimal iris melanin.",
                "detail": "Enhancer inactive, reduced OCA2 expression in iris causing blue eye color."
            }
        },
        "implications": "Blue-eyed individuals may have more UV sensitivity",
        "references": ["Eiberg et al. 2008 Hum Genet"]
    },

    # ============================================================================
    # HAIR AND SKIN
    # ============================================================================

    "rs1805007": {
        "gene": "MC1R",
        "name": "Melanocortin 1 Receptor R151C",
        "chromosome": "16",
        "function": "Melanin type switching (eumelanin vs pheomelanin)",
        "category": "Skin",
        "variants": {
            "CC": {
                "effect": "Red hair variant (homozygous)",
                "traits": "Strong red hair phenotype, very fair skin, high sun sensitivity, significantly increased melanoma and skin cancer risk.",
                "detail": "Complete shift toward pheomelanin (red/yellow pigment) production. Very high UV sensitivity."
            },
            "CT": {
                "effect": "Carrier",
                "traits": "May have red hair or reddish tints, fair skin, increased sun sensitivity and skin cancer risk.",
                "detail": "Partial MC1R loss of function increases UV sensitivity."
            },
            "TT": {
                "effect": "Normal function",
                "traits": "Standard melanin production, typical sun response for ethnic background.",
                "detail": "Normal MC1R signaling favoring eumelanin."
            }
        },
        "implications": "Carriers should be vigilant about sun protection and skin checks",
        "references": ["Valverde et al. 1995 Nature Genet"]
    },

    "rs1805008": {
        "gene": "MC1R",
        "name": "MC1R R160W",
        "chromosome": "16",
        "function": "Additional red hair/fair skin variant",
        "category": "Skin",
        "variants": {
            "CC": {
                "effect": "Homozygous variant",
                "traits": "Strong fair skin and red hair tendency, high melanoma risk.",
                "detail": "Loss of function creating pheomelanin dominance."
            },
            "CT": {
                "effect": "Carrier",
                "traits": "Increased fair skin tendency, moderate melanoma risk increase.",
                "detail": "Partial effect on pigmentation."
            },
            "TT": {
                "effect": "Normal",
                "traits": "Standard pigmentation for background.",
                "detail": "Normal MC1R function."
            }
        },
        "implications": "Enhanced sun protection recommended for carriers",
        "references": ["Bastiaens et al. 2001"]
    },

    "rs1426654": {
        "gene": "SLC24A5",
        "name": "Skin Pigmentation Gene",
        "chromosome": "15",
        "function": "Major gene for light skin in European populations",
        "category": "Skin",
        "variants": {
            "AA": {
                "effect": "European light skin variant",
                "traits": "Lighter skin pigmentation, common in European ancestry.",
                "detail": "This variant is nearly fixed in European populations and strongly associated with light skin."
            },
            "AG": {
                "effect": "Intermediate",
                "traits": "Variable skin pigmentation.",
                "detail": "Mixed pigmentation effect."
            },
            "GG": {
                "effect": "Ancestral variant",
                "traits": "Darker skin pigmentation, typical of African ancestry.",
                "detail": "Original human variant supporting higher melanin production."
            }
        },
        "implications": "Light skin variants have higher UV sensitivity, need sun protection",
        "references": ["Lamason et al. 2005 Science"]
    },

    # ============================================================================
    # MUSCLE AND ATHLETICS
    # ============================================================================

    "rs1815739": {
        "gene": "ACTN3",
        "name": "Alpha-Actinin-3 R577X",
        "chromosome": "11",
        "function": "Fast-twitch muscle fiber protein",
        "category": "Athletics",
        "variants": {
            "CC": {
                "effect": "RR - Full ACTN3 function",
                "traits": "Optimal fast-twitch muscle fiber function. Advantage for power and sprint activities. Found in higher frequency among elite sprinters.",
                "detail": "Full alpha-actinin-3 expression supports explosive power and sprint performance."
            },
            "CT": {
                "effect": "RX - Intermediate",
                "traits": "Balanced muscle fiber characteristics, suited for mixed activities.",
                "detail": "Some ACTN3 expression maintained."
            },
            "TT": {
                "effect": "XX - No ACTN3",
                "traits": "Complete loss of ACTN3. Slight endurance advantage, reduced sprint/power capacity. Found in higher frequency among elite endurance athletes.",
                "detail": "No fast-twitch specific alpha-actinin-3 - compensated by alpha-actinin-2. Shifts muscle toward endurance phenotype."
            }
        },
        "implications": "May guide athletic training focus (power vs endurance)",
        "references": ["Yang et al. 2003 AJHG"]
    },

    "rs1799752": {
        "gene": "ACE",
        "name": "Angiotensin Converting Enzyme I/D",
        "chromosome": "17",
        "function": "Blood pressure regulation and muscle efficiency",
        "category": "Athletics",
        "variants": {
            "DD": {
                "effect": "Higher ACE activity",
                "traits": "Associated with power sports performance, higher blood pressure tendency, potentially better strength training response.",
                "detail": "Insertion/deletion polymorphism - DD has highest ACE activity."
            },
            "ID": {
                "effect": "Intermediate",
                "traits": "Balanced characteristics, suited for mixed activities.",
                "detail": "Intermediate ACE levels."
            },
            "II": {
                "effect": "Lower ACE activity",
                "traits": "Associated with endurance performance, more efficient muscle metabolism, potentially better endurance training response.",
                "detail": "Lower ACE activity associated with improved muscular efficiency and endurance capacity."
            }
        },
        "implications": "May inform training approach; II better for endurance, DD for power",
        "references": ["Montgomery et al. 1998 Nature"]
    },

    "rs4253778": {
        "gene": "PPARA",
        "name": "Peroxisome Proliferator-Activated Receptor Alpha",
        "chromosome": "22",
        "function": "Fatty acid metabolism and energy homeostasis",
        "category": "Athletics",
        "variants": {
            "GG": {
                "effect": "Standard PPARA function",
                "traits": "Normal fatty acid oxidation capacity.",
                "detail": "Baseline lipid metabolism."
            },
            "GC": {
                "effect": "Enhanced fat metabolism",
                "traits": "Improved endurance capacity through better fatty acid utilization.",
                "detail": "Enhanced PPARA activity improves fat oxidation during exercise."
            },
            "CC": {
                "effect": "Highest fat oxidation",
                "traits": "Optimal fat burning capacity, potential endurance advantage.",
                "detail": "Maximum PPARA activity for fatty acid metabolism."
            }
        },
        "implications": "May affect response to endurance training and fat metabolism",
        "references": ["Ahmetov et al. 2006"]
    },

    # ============================================================================
    # LONGEVITY
    # ============================================================================

    "rs429358": {
        "gene": "APOE",
        "name": "Apolipoprotein E ε4 Determinant",
        "chromosome": "19",
        "function": "Lipid metabolism and neurodegeneration",
        "category": "Longevity",
        "variants": {
            "TT": {
                "effect": "ε4/ε4 (with rs7412 CC)",
                "traits": "Highest risk for late-onset Alzheimer's disease (10-15x), elevated cardiovascular risk, reduced longevity on average.",
                "detail": "APOE ε4 homozygosity is the strongest genetic risk factor for late-onset Alzheimer's disease."
            },
            "CT": {
                "effect": "ε4 carrier (one copy)",
                "traits": "3-4x increased Alzheimer's risk, moderately elevated cardiovascular risk.",
                "detail": "Single ε4 allele significantly increases dementia risk."
            },
            "CC": {
                "effect": "No ε4 alleles",
                "traits": "Baseline Alzheimer's risk (depends on ε2/ε3 status).",
                "detail": "Either ε3/ε3 (common) or ε2/ε3 or ε2/ε2 (protective)."
            }
        },
        "implications": "ε4 carriers should focus on cardiovascular health, cognitive engagement, and lifestyle factors",
        "references": ["Corder et al. 1993 Science"]
    },

    "rs7412": {
        "gene": "APOE",
        "name": "Apolipoprotein E ε2 Determinant",
        "chromosome": "19",
        "function": "Defines protective ε2 allele",
        "category": "Longevity",
        "variants": {
            "TT": {
                "effect": "ε2/ε2 (with rs429358 CC)",
                "traits": "Most protective for Alzheimer's, associated with longevity. May have higher triglycerides.",
                "detail": "APOE ε2 is associated with reduced Alzheimer's risk and enhanced longevity."
            },
            "CT": {
                "effect": "ε2 carrier",
                "traits": "Some protection against Alzheimer's disease.",
                "detail": "One ε2 allele provides partial protection."
            },
            "CC": {
                "effect": "No ε2 alleles",
                "traits": "Either ε3/ε3 or ε4 carrier depending on rs429358.",
                "detail": "APOE status determined by combination with rs429358."
            }
        },
        "implications": "ε2 carriers have favorable longevity profile",
        "references": ["Schachter et al. 1994"]
    },

    "rs2802292": {
        "gene": "FOXO3",
        "name": "Forkhead Box O3",
        "chromosome": "6",
        "function": "Longevity-associated transcription factor",
        "category": "Longevity",
        "variants": {
            "GG": {
                "effect": "Longevity variant",
                "traits": "Associated with increased lifespan in multiple populations. Enhanced stress resistance and cellular maintenance.",
                "detail": "The G allele has been consistently associated with exceptional longevity across diverse populations."
            },
            "GT": {
                "effect": "Intermediate",
                "traits": "Some longevity association.",
                "detail": "One copy of longevity-associated allele."
            },
            "TT": {
                "effect": "Common variant",
                "traits": "Standard lifespan genetics at this locus.",
                "detail": "Baseline FOXO3 function."
            }
        },
        "implications": "Part of longevity genetic profile",
        "references": ["Willcox et al. 2008 PNAS"]
    },

    # ============================================================================
    # SLEEP AND CIRCADIAN
    # ============================================================================

    "rs57875989": {
        "gene": "PER2",
        "name": "Period 2 Circadian Clock",
        "chromosome": "2",
        "function": "Core circadian rhythm gene",
        "category": "Sleep",
        "variants": {
            "GG": {
                "effect": "Delayed sleep phase tendency",
                "traits": "May prefer later sleep and wake times, natural 'night owl' tendency.",
                "detail": "Associated with delayed circadian phase."
            },
            "GC": {
                "effect": "Intermediate",
                "traits": "Moderate chronotype.",
                "detail": "Balanced circadian timing."
            },
            "CC": {
                "effect": "Earlier sleep phase",
                "traits": "May prefer earlier sleep and wake times, 'morning lark' tendency.",
                "detail": "Associated with advanced circadian phase."
            }
        },
        "implications": "Understanding chronotype can improve sleep hygiene and scheduling",
        "references": ["Toh et al. 2001 Science"]
    },

    "rs5443": {
        "gene": "GNB3",
        "name": "G-Protein Beta 3 Subunit",
        "chromosome": "12",
        "function": "Signal transduction affecting various body systems",
        "category": "Sleep",
        "variants": {
            "CC": {
                "effect": "CC genotype",
                "traits": "Associated with different sleep architecture, may have more deep sleep.",
                "detail": "Affects G-protein coupled receptor signaling."
            },
            "CT": {
                "effect": "CT genotype",
                "traits": "Intermediate sleep characteristics.",
                "detail": "Mixed signaling effects."
            },
            "TT": {
                "effect": "TT genotype",
                "traits": "Different sleep architecture patterns, may be associated with hypertension.",
                "detail": "Enhanced G-protein signaling, affects multiple systems."
            }
        },
        "implications": "May affect sleep quality and cardiovascular regulation",
        "references": ["Siffert et al. 1998 Nature Genet"]
    }
}

# Gene interaction patterns for medical risk
MEDICAL_INTERACTIONS = {
    "cardiovascular_risk": {
        "genes": ["rs1333049", "rs10757278", "rs4977574", "rs1801133", "rs662"],
        "description": "Comprehensive cardiovascular risk assessment",
        "analysis": """
        Cardiovascular disease risk emerges from multiple genetic pathways. The 9p21 locus
        variants (rs1333049, rs10757278, rs4977574) create a risk haplotype that affects
        cell cycle regulation and vascular smooth muscle proliferation.

        MTHFR variants (rs1801133) affect homocysteine metabolism - elevated homocysteine
        is an independent cardiovascular risk factor that can be modified with B-vitamin
        supplementation.

        PON1 (rs662) affects the protective antioxidant function of HDL cholesterol,
        modifying how diet and oxidative stress impact cardiovascular health.

        Combined risk assessment should integrate all these pathways for comprehensive
        cardiovascular risk management.
        """
    },

    "diabetes_metabolism": {
        "genes": ["rs7903146", "rs1801282", "rs5219", "rs9939609", "rs17782313"],
        "description": "Metabolic health and diabetes risk",
        "analysis": """
        Type 2 diabetes risk involves both insulin secretion (beta cell function) and
        insulin sensitivity (peripheral tissue response).

        TCF7L2 (rs7903146) is the strongest common diabetes risk gene, affecting beta cell
        development and incretin response. KCNJ11 (rs5219) affects insulin secretion through
        potassium channel function.

        PPARG (rs1801282) affects insulin sensitivity - the Ala variant provides protection.

        Obesity genes FTO (rs9939609) and MC4R (rs17782313) increase diabetes risk
        indirectly through weight gain, but their effects can be largely negated through
        physical activity.

        Combined genetic risk can be substantially modified by lifestyle, particularly
        weight management, physical activity, and diet quality.
        """
    },

    "thrombophilia": {
        "genes": ["rs6025", "rs1799963", "rs5985"],
        "description": "Blood clotting disorder risk",
        "analysis": """
        Inherited thrombophilia increases venous thromboembolism (VTE) risk. Factor V Leiden
        (rs6025) and Prothrombin G20210A (rs1799963) are the most clinically significant
        variants.

        Compound heterozygosity (carrying both Factor V Leiden and Prothrombin G20210A)
        creates multiplicative risk - much higher than either variant alone.

        Factor XIII variants (rs5985) modify clot structure and stability, with potential
        protective effects in some contexts.

        Thrombophilia risk is strongly modified by environmental factors - estrogen exposure,
        immobility, surgery, and dehydration all compound genetic risk. Carriers should
        inform all healthcare providers and receive prophylactic anticoagulation in high-risk
        situations.
        """
    },

    "drug_metabolism": {
        "genes": ["rs1799853", "rs1057910", "rs9923231", "rs4244285", "rs1065852"],
        "description": "Pharmacogenomic profile",
        "analysis": """
        Drug metabolism varies dramatically based on genetic variants. CYP2C9 (rs1799853,
        rs1057910) affects warfarin, NSAIDs, and many other drug metabolisms. Combined with
        VKORC1 (rs9923231), these variants determine appropriate warfarin dosing.

        CYP2C19 (rs4244285) is critical for clopidogrel activation - poor metabolizers
        may not benefit from this common antiplatelet drug and may need alternatives.

        CYP2D6 (rs1065852) affects metabolism of approximately 25% of all medications
        including many antidepressants, beta blockers, and opioids.

        Pharmacogenomic information should be shared with all healthcare providers and
        may be crucial for safe and effective medication dosing.
        """
    },

    "inflammation_autoimmune": {
        "genes": ["rs1800795", "rs1800629", "rs2476601", "rs3087243"],
        "description": "Inflammatory and autoimmune tendencies",
        "analysis": """
        Baseline inflammatory state and autoimmune susceptibility involve both cytokine
        production genes and immune regulation genes.

        IL-6 (rs1800795) and TNF-alpha (rs1800629) promoter variants affect inflammatory
        cytokine production. High-production variants create a more pro-inflammatory
        baseline state.

        PTPN22 (rs2476601) and CTLA4 (rs3087243) affect T-cell regulation. Risk variants
        increase susceptibility to multiple autoimmune conditions including rheumatoid
        arthritis, type 1 diabetes, thyroid disease, and lupus.

        Individuals with pro-inflammatory and autoimmune-risk profiles benefit from
        anti-inflammatory lifestyle interventions and should be monitored for early
        signs of autoimmune conditions.
        """
    },

    "nutrient_metabolism": {
        "genes": ["rs1801133", "rs1801394", "rs762551", "rs4988235", "rs7946"],
        "description": "Nutrient processing and dietary needs",
        "analysis": """
        Genetic variants affect how the body processes and utilizes nutrients.

        MTHFR (rs1801133) and MTRR (rs1801394) affect B-vitamin and methylation metabolism.
        Combined reduced-function variants may require higher B-vitamin intake and can affect
        homocysteine levels.

        CYP1A2 (rs762551) determines caffeine metabolism - slow metabolizers should limit
        coffee intake, especially later in the day.

        LCT (rs4988235) determines lactose tolerance - non-persistence genotype requires
        lactose-free alternatives or enzyme supplementation for dairy consumption.

        PEMT (rs7946) affects choline requirements - certain variants increase dietary
        choline needs.

        Understanding these variants allows for personalized nutrition recommendations.
        """
    }
}

MEDICAL_CATEGORIES = {
    "Cardiovascular": "Heart health, blood vessels, and circulation",
    "Diabetes": "Blood sugar regulation and metabolic health",
    "Cancer": "Cancer susceptibility and DNA repair",
    "Pharmacogenomics": "Drug metabolism and medication response",
    "Nutrition": "Nutrient metabolism and dietary needs",
    "Metabolism": "Energy balance and weight regulation",
    "Autoimmune": "Immune system regulation and autoimmune risk",
    "Bone Health": "Bone density and mineral metabolism",
    "Inflammation": "Inflammatory response and chronic inflammation",
    "Clotting": "Blood clotting and thrombosis risk",
    "Vision": "Eye health and vision-related traits",
    "Skin": "Skin pigmentation and UV sensitivity",
    "Athletics": "Muscle composition and athletic potential",
    "Longevity": "Aging and lifespan factors",
    "Sleep": "Sleep patterns and circadian rhythm"
}
