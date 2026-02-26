#!/usr/bin/env python3
"""
Medical DNA Analyzer - Physical and Medical Trait Analysis
Generates detailed PDF books analyzing health-related genetic variants from 23andMe data
"""

import os
import sys
from datetime import datetime
from collections import defaultdict
from medical_snps import MEDICAL_SNPS, MEDICAL_INTERACTIONS, MEDICAL_CATEGORIES

def parse_genome_file(filepath):
    """Parse 23andMe raw data file and return dictionary of rsid -> genotype"""
    genome = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('#'):
                continue
            parts = line.strip().split('\t')
            if len(parts) >= 4:
                rsid = parts[0]
                chromosome = parts[1]
                position = parts[2]
                genotype = parts[3]
                genome[rsid] = {
                    'chromosome': chromosome,
                    'position': position,
                    'genotype': genotype
                }
    return genome

def analyze_medical_snps(genome):
    """Match genome data against medical SNP database"""
    results = {}
    missing = []

    for rsid, snp_info in MEDICAL_SNPS.items():
        if rsid in genome:
            genotype = genome[rsid]['genotype']
            if genotype == '--' or genotype == '':
                missing.append(rsid)
                continue

            matched = False
            for variant_geno, variant_info in snp_info['variants'].items():
                if genotype == variant_geno or genotype == variant_geno[::-1]:
                    results[rsid] = {
                        'gene': snp_info['gene'],
                        'name': snp_info['name'],
                        'chromosome': genome[rsid]['chromosome'],
                        'position': genome[rsid]['position'],
                        'genotype': genotype,
                        'effect': variant_info['effect'],
                        'traits': variant_info['traits'],
                        'detail': variant_info['detail'],
                        'category': snp_info['category'],
                        'function': snp_info['function'],
                        'implications': snp_info.get('implications', ''),
                        'references': snp_info.get('references', [])
                    }
                    matched = True
                    break

            if not matched:
                results[rsid] = {
                    'gene': snp_info['gene'],
                    'name': snp_info['name'],
                    'chromosome': genome[rsid]['chromosome'],
                    'position': genome[rsid]['position'],
                    'genotype': genotype,
                    'effect': f'Uncommon genotype: {genotype}',
                    'traits': 'This genotype is not commonly characterized in the literature.',
                    'detail': 'The observed genotype differs from common variants and may represent a rare or population-specific polymorphism.',
                    'category': snp_info['category'],
                    'function': snp_info['function'],
                    'implications': snp_info.get('implications', ''),
                    'references': snp_info.get('references', [])
                }
        else:
            missing.append(rsid)

    return results, missing

def analyze_medical_interactions(results):
    """Analyze gene-gene interactions for medical risk profiles"""
    interaction_analysis = {}

    for interaction_name, interaction_info in MEDICAL_INTERACTIONS.items():
        present_genes = []
        gene_results = {}

        for rsid in interaction_info['genes']:
            if rsid in results:
                present_genes.append(rsid)
                gene_results[rsid] = results[rsid]

        if len(present_genes) >= 2:
            interaction_analysis[interaction_name] = {
                'description': interaction_info['description'],
                'base_analysis': interaction_info['analysis'],
                'present_genes': present_genes,
                'gene_results': gene_results,
                'coverage': len(present_genes) / len(interaction_info['genes'])
            }

    return interaction_analysis

def categorize_results(results):
    """Group results by medical category"""
    categorized = defaultdict(list)
    for rsid, data in results.items():
        categorized[data['category']].append((rsid, data))
    return categorized

def generate_health_summary(results):
    """Generate overall health risk summary"""
    summary = {
        'cardiovascular': 'average',
        'diabetes': 'average',
        'thrombophilia': 'none_detected',
        'caffeine_metabolism': 'unknown',
        'lactose_tolerance': 'unknown',
        'drug_metabolism_notes': []
    }

    # Cardiovascular assessment
    cv_risk_markers = 0
    if 'rs1333049' in results and results['rs1333049']['genotype'] in ['CC', 'CG', 'GC']:
        cv_risk_markers += 1
    if 'rs1801133' in results and results['rs1801133']['genotype'] in ['AA', 'AG', 'GA']:
        cv_risk_markers += 1

    if cv_risk_markers >= 2:
        summary['cardiovascular'] = 'elevated'
    elif cv_risk_markers == 0:
        summary['cardiovascular'] = 'lower'

    # Diabetes assessment
    if 'rs7903146' in results:
        geno = results['rs7903146']['genotype']
        if geno == 'TT':
            summary['diabetes'] = 'elevated'
        elif geno in ['CT', 'TC']:
            summary['diabetes'] = 'moderate'

    # Thrombophilia
    if 'rs6025' in results:
        geno = results['rs6025']['genotype']
        if geno in ['CC', 'CT', 'TC']:
            summary['thrombophilia'] = 'factor_v_leiden_detected'

    # Caffeine
    if 'rs762551' in results:
        geno = results['rs762551']['genotype']
        if geno == 'AA':
            summary['caffeine_metabolism'] = 'fast'
        else:
            summary['caffeine_metabolism'] = 'slow'

    # Lactose
    if 'rs4988235' in results:
        geno = results['rs4988235']['genotype']
        if geno == 'GG':
            summary['lactose_tolerance'] = 'intolerant'
        else:
            summary['lactose_tolerance'] = 'tolerant'

    # Drug metabolism notes
    if 'rs4244285' in results:
        geno = results['rs4244285']['genotype']
        if geno in ['AA']:
            summary['drug_metabolism_notes'].append('CYP2C19 poor metabolizer - clopidogrel may be ineffective')
    if 'rs1799853' in results and results['rs1799853']['genotype'] in ['TT', 'CT', 'TC']:
        summary['drug_metabolism_notes'].append('CYP2C9 reduced function - warfarin dose reduction may be needed')

    return summary

def generate_medical_markdown(name, results, missing, interactions, summary, genome_file):
    """Generate comprehensive medical analysis markdown"""

    categorized = categorize_results(results)
    timestamp = datetime.now().strftime("%Y-%m-%d")

    md = []

    # Title
    md.append(f"# The Medical DNA Story of {name}")
    md.append("")
    md.append("## A Comprehensive Genetic Health Analysis")
    md.append("")
    md.append(f"*Generated: {timestamp}*")
    md.append("")
    md.append("---")
    md.append("")

    # Important Disclaimer
    md.append("## IMPORTANT MEDICAL DISCLAIMER")
    md.append("")
    md.append("**This genetic analysis is for EDUCATIONAL and INFORMATIONAL purposes only.**")
    md.append("")
    md.append("- This is NOT a medical diagnosis and should NOT be used for medical decision-making")
    md.append("- Genetic risk does NOT equal destiny - lifestyle and environmental factors are crucial")
    md.append("- Many variants have small effect sizes that may not be clinically significant")
    md.append("- Some findings may require clinical confirmation with certified genetic testing")
    md.append("- Always consult qualified healthcare professionals for medical decisions")
    md.append("- Pharmacogenomic findings should be verified before affecting medication choices")
    md.append("")
    md.append("The information provided is based on scientific literature as of the analysis date,")
    md.append("but genetic research is an evolving field. Interpretation may change as science advances.")
    md.append("")
    md.append("---")
    md.append("")

    # Preface
    md.append("## Preface")
    md.append("")
    md.append("> *\"Your genes load the gun, but your lifestyle pulls the trigger.\"*")
    md.append("> *— Common medical genetics saying*")
    md.append("")
    md.append("This book examines genetic variants that influence physical health, disease risk,")
    md.append("and drug metabolism. Unlike the personality analysis, these variants often have more")
    md.append("direct biological effects, though environmental factors remain crucial modifiers.")
    md.append("")
    md.append(f"This analysis examined {len(results)} health-related genetic variants from your genome,")
    md.append(f"with {len(missing)} variants not available in the provided data.")
    md.append("")
    md.append("---")
    md.append("")

    # Table of Contents
    md.append("## Table of Contents")
    md.append("")
    md.append("1. [Executive Health Summary](#executive-health-summary)")
    md.append("2. [Actionable Findings](#actionable-findings)")

    chapter_num = 3
    for category in MEDICAL_CATEGORIES.keys():
        if category in categorized:
            md.append(f"{chapter_num}. [{category}](#{category.lower().replace(' ', '-')})")
            chapter_num += 1

    md.append(f"{chapter_num}. [Gene Interactions & Combined Risk](#gene-interactions--combined-risk)")
    md.append(f"{chapter_num + 1}. [Complete Variant Reference](#complete-variant-reference)")
    md.append(f"{chapter_num + 2}. [Recommendations Summary](#recommendations-summary)")
    md.append("")
    md.append("---")
    md.append("")

    # Executive Summary
    md.append("## Executive Health Summary")
    md.append("")
    md.append(f"### {name}'s Genetic Health Overview")
    md.append("")
    md.append("Based on analysis of health-associated genetic variants:")
    md.append("")
    md.append(f"**Cardiovascular Risk Profile:** {summary['cardiovascular'].replace('_', ' ').title()}")
    md.append(f"**Diabetes Risk Profile:** {summary['diabetes'].replace('_', ' ').title()}")
    md.append(f"**Thrombophilia Status:** {summary['thrombophilia'].replace('_', ' ').title()}")
    md.append(f"**Caffeine Metabolism:** {summary['caffeine_metabolism'].replace('_', ' ').title()}")
    md.append(f"**Lactose Tolerance:** {summary['lactose_tolerance'].replace('_', ' ').title()}")
    md.append("")

    if summary['drug_metabolism_notes']:
        md.append("**Important Drug Metabolism Findings:**")
        for note in summary['drug_metabolism_notes']:
            md.append(f"- {note}")
        md.append("")

    md.append("---")
    md.append("")

    # Actionable Findings
    md.append("## Actionable Findings")
    md.append("")
    md.append("The following findings may have direct implications for your health management:")
    md.append("")

    # Critical findings
    critical_snps = ['rs6025', 'rs1799963', 'rs4244285', 'rs9923231', 'rs1799853', 'rs1057910']
    for rsid in critical_snps:
        if rsid in results:
            r = results[rsid]
            if 'risk' in r['effect'].lower() or 'carrier' in r['effect'].lower() or 'poor' in r['effect'].lower() or 'reduced' in r['effect'].lower():
                md.append(f"### {r['gene']} ({rsid})")
                md.append(f"**Your Genotype:** {r['genotype']} — {r['effect']}")
                md.append("")
                md.append(f"**Significance:** {r['traits']}")
                md.append("")
                if r['implications']:
                    md.append(f"**Recommended Action:** {r['implications']}")
                    md.append("")
                md.append("---")
                md.append("")

    # Detailed Analysis by Category
    for category, description in MEDICAL_CATEGORIES.items():
        if category not in categorized:
            continue

        md.append(f"## {category}")
        md.append("")
        md.append(f"*{description}*")
        md.append("")

        # Category introductions
        category_intros = {
            "Cardiovascular": """
Cardiovascular disease remains the leading cause of death worldwide, but it is also highly
modifiable. The genetic variants examined here affect various aspects of heart and blood vessel
health, including atherosclerosis risk, blood pressure regulation, and lipid metabolism.

Understanding your cardiovascular genetics can guide preventive strategies, including lifestyle
modifications and appropriate screening intervals. However, genetic risk can be substantially
reduced through proper diet, exercise, and medical management when indicated.
""",
            "Diabetes": """
Type 2 diabetes results from the interaction of genetic susceptibility with lifestyle factors.
The variants analyzed here affect both insulin secretion from the pancreas and insulin
sensitivity in peripheral tissues.

Even with elevated genetic risk, type 2 diabetes is often preventable through weight management,
physical activity, and dietary choices. Those with genetic risk benefit most from early
lifestyle intervention.
""",
            "Pharmacogenomics": """
Pharmacogenomics examines how genetic variation affects drug response. These variants can
determine whether you need higher or lower doses of certain medications, whether some drugs
will work for you, and your risk for adverse drug reactions.

**IMPORTANT:** Share these results with your healthcare providers. Pharmacogenomic information
can be crucial for safe and effective prescribing. This is particularly important for:
- Warfarin and other anticoagulants
- Clopidogrel (Plavix) and related antiplatelet drugs
- Many antidepressants and psychiatric medications
- Certain pain medications
- Some cancer drugs
""",
            "Clotting": """
Blood clotting disorders (thrombophilias) increase the risk of dangerous blood clots in veins
(DVT, pulmonary embolism) and sometimes arteries. These conditions are particularly important
to know about before:
- Surgery or prolonged immobility
- Pregnancy or estrogen-based contraception
- Long flights or car trips

Carriers of clotting variants should inform all healthcare providers and may need prophylactic
anticoagulation in certain situations.
""",
            "Cancer": """
Cancer genetics is complex. The variants examined here affect DNA repair capacity and cellular
protection against carcinogens. These are common variants with modest effects, different from
rare high-penetrance mutations in genes like BRCA1/2.

Understanding these variants can guide lifestyle choices and screening decisions, but they
should not cause undue alarm. Most cancer risk comes from environmental factors and can be
modified through lifestyle.
""",
            "Athletics": """
Athletic performance is influenced by genetic variants affecting muscle fiber composition,
oxygen utilization, and recovery capacity. These variants can help guide training approaches
but do not determine athletic success - training, nutrition, and mental factors are equally
or more important.

Understanding your genetic athletic profile can help optimize training by focusing on your
natural strengths or deliberately developing areas of genetic disadvantage.
"""
        }

        if category in category_intros:
            md.append(category_intros[category])
            md.append("")

        md.append("### Your Variants in This Category")
        md.append("")

        for rsid, data in categorized[category]:
            md.append(f"#### {data['gene']} — {data['name']}")
            md.append("")
            md.append(f"**SNP ID:** {rsid}")
            md.append(f"**Location:** Chromosome {data['chromosome']}, Position {data['position']}")
            md.append(f"**Your Genotype:** {data['genotype']}")
            md.append("")
            md.append(f"**Gene Function:** {data['function']}")
            md.append("")
            md.append(f"**Your Variant:** {data['effect']}")
            md.append("")
            md.append(f"**Health Implications:**")
            md.append(f"{data['traits']}")
            md.append("")
            md.append(f"**Mechanism:**")
            md.append(f"{data['detail']}")
            md.append("")

            if data['implications']:
                md.append(f"**Clinical Considerations:**")
                md.append(f"{data['implications']}")
                md.append("")

            if data['references']:
                md.append(f"**References:** {', '.join(data['references'])}")
                md.append("")

            md.append("---")
            md.append("")

    # Interactions
    md.append("## Gene Interactions & Combined Risk")
    md.append("")
    md.append("Medical risk often emerges from multiple genetic factors working together.")
    md.append("This section examines how your specific combination of variants creates")
    md.append("overall risk profiles that may differ from individual variant effects.")
    md.append("")

    for interaction_name, interaction_data in interactions.items():
        md.append(f"### {interaction_data['description']}")
        md.append("")
        md.append(f"**Data Coverage:** {interaction_data['coverage']*100:.0f}% of key genes available")
        md.append("")
        md.append("**Your Relevant Variants:**")
        md.append("")

        for rsid in interaction_data['present_genes']:
            r = interaction_data['gene_results'][rsid]
            md.append(f"- **{r['gene']}** ({rsid}): {r['genotype']} — {r['effect'][:60]}...")
        md.append("")

        md.append("**Integrated Analysis:**")
        md.append("")
        md.append(interaction_data['base_analysis'])
        md.append("")
        md.append("---")
        md.append("")

    # Complete Reference
    md.append("## Complete Variant Reference")
    md.append("")
    md.append("| Gene | SNP | Chr | Position | Genotype | Effect |")
    md.append("|------|-----|-----|----------|----------|--------|")

    for rsid, data in sorted(results.items(), key=lambda x: (x[1]['chromosome'], int(x[1]['position']) if x[1]['position'].isdigit() else 0)):
        effect_short = data['effect'][:45] + "..." if len(data['effect']) > 45 else data['effect']
        md.append(f"| {data['gene']} | {rsid} | {data['chromosome']} | {data['position']} | {data['genotype']} | {effect_short} |")

    md.append("")
    md.append("---")
    md.append("")

    # Recommendations
    md.append("## Recommendations Summary")
    md.append("")
    md.append("Based on your genetic profile, consider the following health strategies:")
    md.append("")

    # Generate personalized recommendations
    recommendations = []

    if summary['cardiovascular'] == 'elevated':
        recommendations.append("**Cardiovascular Health:** Prioritize heart health through regular exercise, Mediterranean-style diet, blood pressure monitoring, and lipid panel screening. Consider earlier and more frequent cardiovascular screening.")

    if summary['diabetes'] == 'elevated':
        recommendations.append("**Diabetes Prevention:** Focus on weight management, regular physical activity, and blood glucose monitoring. Limit refined carbohydrates and maintain healthy body weight. Consider annual glucose screening.")

    if 'factor_v_leiden' in summary['thrombophilia']:
        recommendations.append("**Thrombophilia Management:** CRITICAL - Inform all healthcare providers of Factor V Leiden status. Avoid estrogen-based contraceptives. Use compression stockings for long flights. Stay hydrated and mobile during travel. Request prophylactic anticoagulation for surgery or immobility.")

    if summary['caffeine_metabolism'] == 'slow':
        recommendations.append("**Caffeine Intake:** As a slow caffeine metabolizer, limit coffee to 1-2 cups daily and avoid caffeine after noon. Consider that excess caffeine may increase cardiovascular risk.")

    if summary['lactose_tolerance'] == 'intolerant':
        recommendations.append("**Dairy Consumption:** Your genetics indicate lactose intolerance. Use lactose-free products, lactase enzyme supplements, or alternative calcium sources to maintain bone health without digestive discomfort.")

    if summary['drug_metabolism_notes']:
        recommendations.append("**Medication Considerations:** Share your pharmacogenomic profile with prescribers. Key findings: " + "; ".join(summary['drug_metabolism_notes']))

    # Add MTHFR recommendations if applicable
    if 'rs1801133' in results and results['rs1801133']['genotype'] in ['AA', 'AG', 'GA']:
        recommendations.append("**B-Vitamin Needs:** Your MTHFR variant may benefit from adequate folate, B12, and B6 intake. Consider methylated forms of folate (methylfolate) rather than folic acid. Monitor homocysteine if concerned about cardiovascular risk.")

    if not recommendations:
        recommendations.append("No critical action items identified. Continue standard health maintenance with regular checkups.")

    for rec in recommendations:
        md.append(rec)
        md.append("")

    md.append("---")
    md.append("")

    # Closing
    md.append("## Afterword")
    md.append("")
    md.append("This medical genetic analysis provides a foundation for understanding your")
    md.append("inherited health tendencies. Remember that genetics is only one factor in health —")
    md.append("lifestyle, environment, and medical care are equally or more important for most conditions.")
    md.append("")
    md.append("Use this information to have informed conversations with your healthcare providers,")
    md.append("make evidence-based lifestyle choices, and prioritize appropriate preventive care.")
    md.append("")
    md.append(f"*Analysis generated from: {os.path.basename(genome_file)}*")
    md.append("")
    md.append("---")
    md.append("")
    md.append("*DNA Analyzer — Medical Genetic Health Analysis*")
    md.append("")

    return '\n'.join(md)


def main():
    if len(sys.argv) < 3:
        print("Usage: python medical_analyzer.py <genome_file> <subject_name>")
        sys.exit(1)

    genome_file = sys.argv[1]
    subject_name = sys.argv[2]

    print(f"Analyzing genome for: {subject_name}")
    print(f"Reading genome file: {genome_file}")

    genome = parse_genome_file(genome_file)
    print(f"Parsed {len(genome)} SNPs from genome file")

    results, missing = analyze_medical_snps(genome)
    print(f"Found {len(results)} health-related variants")
    print(f"Missing {len(missing)} variants from database")

    interactions = analyze_medical_interactions(results)
    print(f"Analyzed {len(interactions)} gene interaction patterns")

    summary = generate_health_summary(results)
    print("Generated health summary")

    markdown_content = generate_medical_markdown(subject_name, results, missing, interactions, summary, genome_file)

    safe_name = subject_name.replace(' ', '_')
    output_file = f"books/Medical_DNA_Story_{safe_name}.md"
    os.makedirs('books', exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content)

    print(f"Saved medical analysis to: {output_file}")
    return output_file


if __name__ == "__main__":
    main()
