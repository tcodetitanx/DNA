#!/usr/bin/env python3
"""
DNA Analyzer - Comprehensive Genome Personality Analysis
Generates detailed PDF books analyzing personality traits from 23andMe raw data
"""

import os
import sys
from datetime import datetime
from collections import defaultdict
from personality_snps import PERSONALITY_SNPS, GENE_INTERACTIONS, TRAIT_CATEGORIES

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

def analyze_personality_snps(genome):
    """Match genome data against personality SNP database"""
    results = {}
    missing = []

    for rsid, snp_info in PERSONALITY_SNPS.items():
        if rsid in genome:
            genotype = genome[rsid]['genotype']
            # Handle different genotype formats
            if genotype == '--' or genotype == '':
                missing.append(rsid)
                continue

            # Try to match genotype
            matched = False
            for variant_geno, variant_info in snp_info['variants'].items():
                # Check both orientations (AB and BA)
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
                        'interactions': snp_info.get('interactions', []),
                        'references': snp_info.get('references', [])
                    }
                    matched = True
                    break

            if not matched:
                # Record the genotype even if not in our database
                results[rsid] = {
                    'gene': snp_info['gene'],
                    'name': snp_info['name'],
                    'chromosome': genome[rsid]['chromosome'],
                    'position': genome[rsid]['position'],
                    'genotype': genotype,
                    'effect': f'Novel/Rare genotype: {genotype}',
                    'traits': 'This genotype is not well characterized in the literature.',
                    'detail': 'The observed genotype differs from common variants. This may represent a rare variant or population-specific polymorphism.',
                    'category': snp_info['category'],
                    'function': snp_info['function'],
                    'interactions': snp_info.get('interactions', []),
                    'references': snp_info.get('references', [])
                }
        else:
            missing.append(rsid)

    return results, missing

def analyze_interactions(results):
    """Analyze gene-gene interactions for emergent traits"""
    interaction_analysis = {}

    for interaction_name, interaction_info in GENE_INTERACTIONS.items():
        present_genes = []
        gene_results = {}

        for rsid in interaction_info['genes']:
            if rsid in results:
                present_genes.append(rsid)
                gene_results[rsid] = results[rsid]

        if len(present_genes) >= 2:  # Need at least 2 genes for interaction
            interaction_analysis[interaction_name] = {
                'description': interaction_info['description'],
                'base_analysis': interaction_info['analysis'],
                'present_genes': present_genes,
                'gene_results': gene_results,
                'coverage': len(present_genes) / len(interaction_info['genes'])
            }

    return interaction_analysis

def categorize_results(results):
    """Group results by trait category"""
    categorized = defaultdict(list)
    for rsid, data in results.items():
        categorized[data['category']].append((rsid, data))
    return categorized

def generate_trait_summary(results):
    """Generate overall personality trait summary"""
    summary = {
        'emotional_sensitivity': 'moderate',
        'stress_resilience': 'moderate',
        'social_orientation': 'moderate',
        'cognitive_style': 'balanced',
        'reward_sensitivity': 'moderate',
        'creativity_potential': 'moderate',
        'chronotype': 'intermediate'
    }

    # Analyze emotional sensitivity
    emotional_markers = []
    if 'rs25531' in results:
        if results['rs25531']['genotype'] in ['AA', 'AG', 'GA']:
            emotional_markers.append('high')
        else:
            emotional_markers.append('low')
    if 'rs6295' in results:
        if results['rs6295']['genotype'] in ['CC']:
            emotional_markers.append('high')
        else:
            emotional_markers.append('low')
    if emotional_markers:
        summary['emotional_sensitivity'] = 'high' if emotional_markers.count('high') > emotional_markers.count('low') else 'low'

    # Analyze stress resilience
    stress_markers = []
    if 'rs4680' in results:
        if results['rs4680']['genotype'] in ['GG']:
            stress_markers.append('high')
        elif results['rs4680']['genotype'] in ['AA']:
            stress_markers.append('low')
        else:
            stress_markers.append('moderate')
    if 'rs110402' in results:
        if results['rs110402']['genotype'] in ['AA']:
            stress_markers.append('high')
        else:
            stress_markers.append('moderate')
    if stress_markers:
        if stress_markers.count('high') >= len(stress_markers) / 2:
            summary['stress_resilience'] = 'high'
        elif stress_markers.count('low') >= len(stress_markers) / 2:
            summary['stress_resilience'] = 'low'

    # Analyze social orientation
    social_markers = []
    if 'rs53576' in results:
        if results['rs53576']['genotype'] in ['GG']:
            social_markers.append('high')
        elif results['rs53576']['genotype'] in ['AA']:
            social_markers.append('low')
        else:
            social_markers.append('moderate')
    if social_markers:
        summary['social_orientation'] = social_markers[0]

    # Analyze cognitive style
    if 'rs4680' in results:
        if results['rs4680']['genotype'] in ['AA']:
            summary['cognitive_style'] = 'analytical/deliberative'
        elif results['rs4680']['genotype'] in ['GG']:
            summary['cognitive_style'] = 'action-oriented/intuitive'
        else:
            summary['cognitive_style'] = 'balanced'

    # Analyze reward sensitivity
    reward_markers = []
    if 'rs1800497' in results:
        if results['rs1800497']['genotype'] in ['TT', 'CT', 'TC']:
            reward_markers.append('high')
        else:
            reward_markers.append('normal')
    if reward_markers:
        summary['reward_sensitivity'] = reward_markers[0]

    return summary

def generate_markdown_book(name, results, missing, interactions, summary, genome_file):
    """Generate comprehensive markdown analysis book"""

    categorized = categorize_results(results)
    timestamp = datetime.now().strftime("%Y-%m-%d")

    md = []

    # Title Page
    md.append(f"# The DNA Story of {name}")
    md.append("")
    md.append("## A Comprehensive Genetic Personality Analysis")
    md.append("")
    md.append(f"*Generated: {timestamp}*")
    md.append("")
    md.append("---")
    md.append("")

    # Dedication/Epigraph
    md.append("## Preface")
    md.append("")
    md.append("> *\"In the twisted ladder of DNA, we find not our destiny, but our tendencies—")
    md.append("> the whispered suggestions of a billion years of evolution, waiting to be")
    md.append("> heard or overwritten by the choices we make.\"*")
    md.append("")
    md.append("This book represents a comprehensive analysis of the genetic variants that influence")
    md.append("personality, cognition, and behavior. The analysis is based on peer-reviewed scientific")
    md.append("research examining Single Nucleotide Polymorphisms (SNPs) associated with psychological traits.")
    md.append("")
    md.append("**Important Considerations:**")
    md.append("")
    md.append("1. **Genetics is not destiny.** Environmental factors, life experiences, and personal choices")
    md.append("   profoundly shape who we become. Genes create tendencies, not certainties.")
    md.append("")
    md.append("2. **Complex traits are polygenic.** Personality emerges from thousands of genetic variants,")
    md.append("   each contributing a small effect. No single gene determines any personality trait.")
    md.append("")
    md.append("3. **Gene-environment interaction is crucial.** The same genetic variant may have different")
    md.append("   effects depending on life circumstances—this is known as differential susceptibility.")
    md.append("")
    md.append("4. **Scientific understanding continues to evolve.** New research regularly refines our")
    md.append("   understanding of genetic influences on behavior.")
    md.append("")
    md.append(f"This analysis examined {len(results)} personality-related genetic variants from the")
    md.append(f"genome data file, with {len(missing)} variants not available in the data.")
    md.append("")
    md.append("---")
    md.append("")

    # Table of Contents
    md.append("## Table of Contents")
    md.append("")
    md.append("1. [Executive Summary](#executive-summary)")
    md.append("2. [Personality Profile Overview](#personality-profile-overview)")

    chapter_num = 3
    for category in TRAIT_CATEGORIES.keys():
        if category in categorized:
            md.append(f"{chapter_num}. [{category}](#{category.lower().replace(' ', '-')})")
            chapter_num += 1

    md.append(f"{chapter_num}. [Gene Interactions & Emergent Traits](#gene-interactions--emergent-traits)")
    md.append(f"{chapter_num + 1}. [Complete Variant Reference](#complete-variant-reference)")
    md.append(f"{chapter_num + 2}. [Scientific References](#scientific-references)")
    md.append("")
    md.append("---")
    md.append("")

    # Executive Summary
    md.append("## Executive Summary")
    md.append("")
    md.append(f"### {name}'s Genetic Personality Signature")
    md.append("")
    md.append("Based on analysis of personality-associated genetic variants, the following")
    md.append("tendencies emerge from your DNA:")
    md.append("")
    md.append(f"**Emotional Sensitivity:** {summary['emotional_sensitivity'].title()}")
    md.append(f"**Stress Resilience:** {summary['stress_resilience'].title()}")
    md.append(f"**Social Orientation:** {summary['social_orientation'].title()}")
    md.append(f"**Cognitive Style:** {summary['cognitive_style'].title()}")
    md.append(f"**Reward Sensitivity:** {summary['reward_sensitivity'].title()}")
    md.append("")

    # Key findings
    md.append("### Key Genetic Findings")
    md.append("")

    key_genes = ['rs4680', 'rs25531', 'rs53576', 'rs6265', 'rs1800497', 'rs6323']
    for rsid in key_genes:
        if rsid in results:
            r = results[rsid]
            md.append(f"**{r['gene']} ({rsid}):** {r['genotype']}")
            md.append(f"- {r['effect']}")
            md.append("")

    md.append("---")
    md.append("")

    # Personality Profile Overview
    md.append("## Personality Profile Overview")
    md.append("")
    md.append("### The Genetic Foundation of Personality")
    md.append("")
    md.append("Your personality emerges from the interplay of genetic predispositions and life experiences.")
    md.append("The genetic variants analyzed here influence neurotransmitter systems that shape how you:")
    md.append("")
    md.append("- Process emotions and respond to stress")
    md.append("- Seek rewards and maintain motivation")
    md.append("- Form social bonds and experience empathy")
    md.append("- Learn, remember, and adapt to new situations")
    md.append("- Regulate impulses and make decisions")
    md.append("")
    md.append("The following chapters examine each neurotransmitter system and trait category in detail,")
    md.append("explaining what your specific variants mean for your psychological tendencies.")
    md.append("")

    # Generate integrated narrative
    md.append("### Integrated Personality Narrative")
    md.append("")

    # Build narrative based on key findings
    narrative_parts = []

    if 'rs4680' in results:
        geno = results['rs4680']['genotype']
        if geno == 'AA':
            narrative_parts.append("Your COMT Met/Met genotype suggests a cognitive style oriented toward deep, analytical thinking. You likely excel at tasks requiring sustained attention and detailed processing, though you may find high-pressure situations more challenging than others do. Your prefrontal cortex maintains higher dopamine levels, supporting complex reasoning but potentially increasing vulnerability to stress-induced cognitive disruption.")
        elif geno == 'GG':
            narrative_parts.append("Your COMT Val/Val genotype indicates a 'Warrior' cognitive style—you likely perform well under pressure and in high-stakes situations. Your efficient dopamine clearance helps maintain cognitive stability during stress, though you may need to work harder on tasks requiring sustained, low-arousal concentration.")
        else:
            narrative_parts.append("Your COMT Val/Met genotype provides a balanced cognitive profile. You can adapt to both high-pressure situations and tasks requiring sustained focus, representing an intermediate phenotype between the 'Worrier' and 'Warrior' styles.")

    if 'rs25531' in results:
        geno = results['rs25531']['genotype']
        if geno in ['AA', 'AG', 'GA']:
            narrative_parts.append("Your serotonin transporter variant suggests heightened emotional sensitivity. You likely experience emotions with greater intensity and depth, responding strongly to both positive and negative environmental influences. This sensitivity can be a source of both vulnerability and strength—you may be more affected by adversity but also more responsive to supportive environments and meaningful experiences.")
        elif geno == 'GG':
            narrative_parts.append("Your serotonin transporter variant indicates greater emotional resilience. You likely maintain mood stability across varying circumstances, with a natural buffer against environmental stressors. While this provides protection against anxiety and depression, you may sometimes miss subtle emotional cues that others readily perceive.")

    if 'rs53576' in results:
        geno = results['rs53576']['genotype']
        if geno == 'GG':
            narrative_parts.append("Your oxytocin receptor genotype suggests strong social orientation. You likely experience empathy deeply, find social connection rewarding, and are attuned to others' emotional states. Social support may be particularly important for your wellbeing, and you may find isolation more challenging than others.")
        elif geno == 'AA':
            narrative_parts.append("Your oxytocin receptor genotype suggests a more self-contained social style. While you certainly can and do form meaningful relationships, you may be more comfortable with solitude and less dependent on social validation than those with high-expression variants. You likely approach relationships pragmatically.")

    if 'rs6265' in results:
        geno = results['rs6265']['genotype']
        if geno == 'GG':
            narrative_parts.append("Your BDNF Val/Val genotype supports optimal neuroplasticity. You likely learn and adapt readily, form new memories efficiently, and can effectively unlearn fear responses and outdated habits. This cognitive flexibility is an asset for personal growth and adaptation to new circumstances.")
        elif geno == 'AA':
            narrative_parts.append("Your BDNF Met/Met genotype suggests a different pattern of neuroplasticity. While you may find some types of learning and habit change more challenging, you likely excel at maintaining established patterns and procedural skills. Once you learn something, you retain it well.")

    for part in narrative_parts:
        md.append(part)
        md.append("")

    md.append("---")
    md.append("")

    # Detailed Category Analysis
    for category, description in TRAIT_CATEGORIES.items():
        if category not in categorized:
            continue

        md.append(f"## {category}")
        md.append("")
        md.append(f"*{description}*")
        md.append("")

        # Category introduction
        category_intros = {
            "Serotonin System": """
The serotonin system is often called the "mood neurotransmitter" system, though its functions extend far
beyond simple happiness. Serotonin regulates emotional responses, anxiety, sleep, appetite, and social
behavior. The genes in this system affect how serotonin is produced, how long it remains active in
synapses, and how sensitive your neurons are to its signals.

Your serotonin system genetics shape your baseline emotional tone, your sensitivity to stress, and
how you process both positive and negative experiences. These variants interact with life experiences
in powerful ways—the same genetic profile that creates vulnerability to depression in harsh environments
may create exceptional emotional depth and creativity in supportive ones.
""",
            "Dopamine System": """
The dopamine system drives motivation, reward-seeking, and executive function. It's the neurochemical
foundation of wanting, striving, and the pleasure of achievement. These genes determine how much
dopamine is available in your brain, how sensitive your neurons are to it, and how quickly it's
cleared from synapses.

Your dopamine genetics influence whether you're more of a "thinker" or "doer," how intensely you
experience rewards, and your vulnerability to addictive patterns. The prefrontal dopamine balance
particularly affects your cognitive style—whether you're more analytical or action-oriented.
""",
            "MAO System": """
Monoamine oxidase enzymes break down neurotransmitters including serotonin, dopamine, and norepinephrine.
These "metabolic" genes act as volume controls on your entire emotional and motivational system.
Low MAO activity means neurotransmitters persist longer, creating more intense emotional experiences.

The famous "Warrior Gene" (MAO-A) earned its name from associations with aggression, but this is an
oversimplification. Low MAO-A activity creates emotional intensity that can manifest as aggression
in adverse environments or as passion and drive in supportive ones. Context matters enormously.
""",
            "Oxytocin System": """
The oxytocin system is the biological foundation of social bonding, trust, and empathy. These genes
determine how much oxytocin is released during social interactions and how sensitive your brain is
to its effects.

Your oxytocin genetics shape how you approach relationships, how deeply you experience empathy,
and how much social connection you need for wellbeing. Some people are genetically wired to thrive
on social closeness, while others function well with more independence.
""",
            "Neuroplasticity": """
Brain-Derived Neurotrophic Factor (BDNF) is crucial for neuron survival, growth, and adaptation.
It's the molecular basis of neuroplasticity—your brain's ability to change in response to experience.

Your BDNF genetics affect how readily you learn new things, how well you remember experiences,
and how easily you can unlearn outdated patterns. High BDNF function supports cognitive flexibility,
while lower function may favor stability and consistency.
""",
            "Stress Response": """
The HPA (Hypothalamic-Pituitary-Adrenal) axis is your body's stress response system. These genes
determine how your body reacts to threats and challenges, how high your cortisol rises, and how
quickly you recover after stress passes.

Your stress genetics don't just affect how stressed you feel—they shape your entire relationship
with challenge and adversity. Some people are wired for quick activation and recovery, while others
have slower, more persistent stress responses.
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
            md.append(f"**Function:** {data['function']}")
            md.append("")
            md.append(f"**Your Variant Effect:** {data['effect']}")
            md.append("")
            md.append(f"**Trait Implications:**")
            md.append(f"{data['traits']}")
            md.append("")
            md.append(f"**Scientific Detail:**")
            md.append(f"{data['detail']}")
            md.append("")

            if data['interactions']:
                interacting_present = [i for i in data['interactions'] if i in results]
                if interacting_present:
                    md.append(f"**Interactions with Other Genes:**")
                    for interact_rsid in interacting_present:
                        if interact_rsid in results:
                            interact_data = results[interact_rsid]
                            md.append(f"- {interact_data['gene']} ({interact_rsid}): Your {interact_data['genotype']} genotype")
                    md.append("")

            if data['references']:
                md.append(f"**Key References:** {', '.join(data['references'])}")
                md.append("")

            md.append("---")
            md.append("")

    # Gene Interactions Chapter
    md.append("## Gene Interactions & Emergent Traits")
    md.append("")
    md.append("### The Whole Is Greater Than the Sum of Its Parts")
    md.append("")
    md.append("Individual gene variants tell only part of the story. Personality traits emerge from")
    md.append("the interaction of multiple genes working together as systems. This chapter examines")
    md.append("how your specific combination of variants creates emergent patterns not predictable")
    md.append("from any single gene alone.")
    md.append("")

    for interaction_name, interaction_data in interactions.items():
        md.append(f"### {interaction_data['description'].title()}")
        md.append("")
        md.append(f"**Interaction Coverage:** {interaction_data['coverage']*100:.0f}% of key genes available")
        md.append("")
        md.append("**Your Relevant Variants:**")
        md.append("")

        for rsid in interaction_data['present_genes']:
            r = interaction_data['gene_results'][rsid]
            md.append(f"- **{r['gene']}** ({rsid}): {r['genotype']} — {r['effect']}")
        md.append("")

        # Generate specific interaction analysis
        md.append("**Analysis:**")
        md.append("")
        md.append(interaction_data['base_analysis'])
        md.append("")

        # Generate personalized interpretation
        md.append("**Your Specific Pattern:**")
        md.append("")

        if interaction_name == "stress_sensitivity":
            comt = interaction_data['gene_results'].get('rs4680', {}).get('genotype', '')
            sert = interaction_data['gene_results'].get('rs25531', {}).get('genotype', '')

            if comt == 'AA' and sert in ['AA', 'AG']:
                md.append("Your combination of Met/Met COMT with low-expression serotonin transporter creates")
                md.append("a profile of high sensitivity. You likely experience emotions deeply, think carefully")
                md.append("before acting, and are strongly affected by your environment. In supportive contexts,")
                md.append("this pattern supports exceptional emotional intelligence and creative thinking. Under")
                md.append("chronic stress, however, you may be more vulnerable than average to anxiety or depression.")
                md.append("Prioritizing stress management and supportive relationships is especially important for you.")
            elif comt == 'GG' and sert == 'GG':
                md.append("Your combination of Val/Val COMT with high-expression serotonin transporter creates")
                md.append("a resilient, action-oriented profile. You likely handle pressure well, recover quickly")
                md.append("from setbacks, and maintain emotional equilibrium across circumstances. While this")
                md.append("provides excellent stress protection, you may sometimes miss opportunities for deeper")
                md.append("emotional processing or reflection.")
            else:
                md.append("Your intermediate pattern provides a balanced stress-sensitivity profile. You have")
                md.append("access to both deep emotional processing and practical stress tolerance, depending")
                md.append("on the situation. This flexibility is an asset, though you may need to consciously")
                md.append("choose which mode to engage depending on circumstances.")

        elif interaction_name == "social_bonding":
            oxtr = interaction_data['gene_results'].get('rs53576', {}).get('genotype', '')
            oprm1 = interaction_data['gene_results'].get('rs1799971', {}).get('genotype', '')

            if oxtr == 'GG':
                md.append("Your GG oxytocin receptor genotype places you high on social orientation. You likely")
                md.append("find social connection deeply rewarding, experience empathy strongly, and are attuned")
                md.append("to others' emotional states. Social support is especially important for your wellbeing.")
                if oprm1 == 'GG':
                    md.append("Combined with your reduced mu-opioid receptor function, you may need to work harder")
                    md.append("to derive comfort from social bonds, but when you do connect, the bonds are meaningful.")
            elif oxtr == 'AA':
                md.append("Your AA oxytocin receptor genotype suggests a more self-contained social style. You can")
                md.append("form deep relationships but may be more comfortable with independence and solitude than")
                md.append("those with high-expression variants. You likely don't need constant social validation.")

        elif interaction_name == "cognitive_style":
            comt = interaction_data['gene_results'].get('rs4680', {}).get('genotype', '')
            bdnf = interaction_data['gene_results'].get('rs6265', {}).get('genotype', '')
            kibra = interaction_data['gene_results'].get('rs17070145', {}).get('genotype', '')

            if comt == 'AA' and bdnf == 'GG':
                md.append("Your Met/Met COMT combined with Val/Val BDNF creates an optimal cognitive profile for")
                md.append("complex analytical work. You have both high prefrontal dopamine supporting working memory")
                md.append("and excellent neuroplasticity supporting learning and adaptation. You likely excel at")
                md.append("academic or intellectual pursuits, though high-pressure timed tests may be challenging.")
            elif comt == 'GG' and bdnf == 'AA':
                md.append("Your Val/Val COMT combined with Met/Met BDNF creates a profile suited for performance")
                md.append("under pressure and procedural learning. You may excel at skills requiring consistent")
                md.append("execution and may maintain expertise once acquired better than those with high plasticity.")

        md.append("")
        md.append("---")
        md.append("")

    # Complete Variant Reference
    md.append("## Complete Variant Reference")
    md.append("")
    md.append("The following table provides a complete reference of all analyzed variants.")
    md.append("")
    md.append("| Gene | SNP | Chr | Position | Genotype | Effect |")
    md.append("|------|-----|-----|----------|----------|--------|")

    for rsid, data in sorted(results.items(), key=lambda x: (x[1]['chromosome'], int(x[1]['position']) if x[1]['position'].isdigit() else 0)):
        effect_short = data['effect'][:50] + "..." if len(data['effect']) > 50 else data['effect']
        md.append(f"| {data['gene']} | {rsid} | {data['chromosome']} | {data['position']} | {data['genotype']} | {effect_short} |")

    md.append("")
    md.append("---")
    md.append("")

    # Scientific References
    md.append("## Scientific References")
    md.append("")
    md.append("The analysis in this book is based on the following peer-reviewed scientific literature:")
    md.append("")

    all_references = set()
    for rsid, data in results.items():
        for ref in data.get('references', []):
            all_references.add(ref)

    for ref in sorted(all_references):
        md.append(f"- {ref}")
    md.append("")

    # Closing
    md.append("---")
    md.append("")
    md.append("## Afterword")
    md.append("")
    md.append("This analysis represents a snapshot of current scientific understanding of personality genetics.")
    md.append("The field continues to evolve rapidly, with new discoveries regularly refining our understanding")
    md.append("of how genes influence who we become.")
    md.append("")
    md.append("Remember that you are not defined by your DNA. These variants create tendencies, not destinies.")
    md.append("Your choices, experiences, relationships, and personal growth all shape your personality in")
    md.append("ways that no genetic analysis can capture.")
    md.append("")
    md.append("Use this information as a tool for self-understanding, not as a limitation. Understanding your")
    md.append("genetic tendencies can help you recognize your strengths, anticipate challenges, and make")
    md.append("informed choices about how to live a life aligned with your authentic self.")
    md.append("")
    md.append(f"*Analysis generated from: {os.path.basename(genome_file)}*")
    md.append("")
    md.append("---")
    md.append("")
    md.append("*DNA Analyzer — Comprehensive Genome Personality Analysis*")
    md.append("")

    return '\n'.join(md)


def main():
    if len(sys.argv) < 3:
        print("Usage: python genome_analyzer.py <genome_file> <subject_name>")
        sys.exit(1)

    genome_file = sys.argv[1]
    subject_name = sys.argv[2]

    print(f"Analyzing genome for: {subject_name}")
    print(f"Reading genome file: {genome_file}")

    # Parse genome
    genome = parse_genome_file(genome_file)
    print(f"Parsed {len(genome)} SNPs from genome file")

    # Analyze personality SNPs
    results, missing = analyze_personality_snps(genome)
    print(f"Found {len(results)} personality-related variants")
    print(f"Missing {len(missing)} variants from database")

    # Analyze interactions
    interactions = analyze_interactions(results)
    print(f"Analyzed {len(interactions)} gene interaction patterns")

    # Generate summary
    summary = generate_trait_summary(results)
    print("Generated personality summary")

    # Generate markdown book
    markdown_content = generate_markdown_book(subject_name, results, missing, interactions, summary, genome_file)

    # Save markdown file
    safe_name = subject_name.replace(' ', '_')
    output_file = f"books/DNA_Story_{safe_name}.md"
    os.makedirs('books', exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content)

    print(f"Saved analysis to: {output_file}")
    return output_file


if __name__ == "__main__":
    main()
