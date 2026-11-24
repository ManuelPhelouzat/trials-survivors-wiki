# Caractéristiques

Les descriptions issues du jeu indiquent le rôle annoncé. Les formules ci-dessous sont des expressions sérialisées vérifiées pour Boule de Givre. L’application en partie, les bornes et le cumul restent à confirmer.

<a href="@alternate/">English</a>

## <img class="stat-icon" src="../public-assets/stats/3d1b8135c0792796b6d5d9016c5f2633b1d6b574aef42b684f3f2d461f0b6706.png" alt="" loading="lazy"> Accélération des Compétences &#40;%&#41; { #stat--858402365 }

Identifiant · ` -858402365 `

**Description du jeu** · Influence le temps de recharge de tes compétences, pour chaque 100 d’Accélération des Compétences, les temps de recharge sont réduits de moitié\.

**Unité** · Pourcentage (fraction sérialisée)

- Calcul de la recharge · ` (GetStat(source,-1565260718)/(1+GetStat(source,-858402365))) ` · PathID 16592
  - source · ` -1565260718 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat--1565260718"><img class="stat-icon" src="../public-assets/stats/08b283c173ddeee4d0c9da754febd02c1f119216a91506d9b67faef2c285c77f.png" alt="" loading="lazy"> Recharge</a>
  - source · ` -858402365 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat--858402365"><img class="stat-icon" src="../public-assets/stats/3d1b8135c0792796b6d5d9016c5f2633b1d6b574aef42b684f3f2d461f0b6706.png" alt="" loading="lazy"> Accélération des Compétences (%)</a>

Source Unity · ` Stat_Description_AbilityHaste ` · ` data.unity3d::sharedassets0.assets ` · PathID 16444

## <span class="stat-icon-missing" role="img" aria-label="Icône non vérifiée" title="Icône non vérifiée">◇</span> Capacité de sursoin &#40;%&#41; { #stat-1910202602 }

Identifiant · ` 1910202602 `

Fonctionnement précis à confirmer.

**Unité** · Pourcentage (fraction sérialisée)

Source Unity · ` data.unity3d::sharedassets0.assets ` · PathID 16491

## <img class="stat-icon" src="../public-assets/stats/32d42a9c52e20b9621925a0c55f7d2586294d8f9964338c247a665579ee8d903.png" alt="" loading="lazy"> Chance de Brûlure { #stat--241968088 }

Identifiant · ` -241968088 `

**Description du jeu** · Augmente les chances d’infliger la Brûlure en touchant un ennemi, infligeant des dégâts sur la durée proportionnels aux dégâts initiaux\.

**Unité** · Pourcentage (fraction sérialisée)

Source Unity · ` Stat_Description_IgniteChance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16476

## <img class="stat-icon" src="../public-assets/stats/32d42a9c52e20b9621925a0c55f7d2586294d8f9964338c247a665579ee8d903.png" alt="" loading="lazy"> Chance de Brûlure &#40;%&#41; { #stat--1810387509 }

Identifiant · ` -1810387509 `

**Description du jeu** · Augmente les chances d’infliger la Brûlure en touchant un ennemi, infligeant des dégâts sur la durée proportionnels aux dégâts initiaux\.

**Unité** · Pourcentage (fraction sérialisée)

Source Unity · ` Stat_Description_IgniteChance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16475

## <img class="stat-icon" src="../public-assets/stats/6c8b3562affd49461eca1ba701afb08874382cae8617808fc932f067a57c3bc1.png" alt="" loading="lazy"> Chance de Choc { #stat--201340349 }

Identifiant · ` -201340349 `

**Description du jeu** · Augmente les chances d’infliger Choc en touchant un ennemi, multipliant les dégâts subis par 50 % et infligeant des dégâts\.

**Unité** · Pourcentage (fraction sérialisée)

Source Unity · ` Stat_Description_ShockChance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16513

## <img class="stat-icon" src="../public-assets/stats/6c8b3562affd49461eca1ba701afb08874382cae8617808fc932f067a57c3bc1.png" alt="" loading="lazy"> Chance de Choc &#40;%&#41; { #stat-883058374 }

Identifiant · ` 883058374 `

**Description du jeu** · Augmente les chances d’infliger Choc en touchant un ennemi, multipliant les dégâts subis par 50 % et infligeant des dégâts\.

**Unité** · Pourcentage (fraction sérialisée)

Source Unity · ` Stat_Description_ShockChance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16512

## <img class="stat-icon" src="../public-assets/stats/67c949ee0937605db9c9fd0295ac69b6e0624a2dd7572fe662ae5954dcd2ccc5.png" alt="" loading="lazy"> Chance de coup critique { #stat-967725324 }

Identifiant · ` 967725324 `

Fonctionnement précis à confirmer.

**Unité** · Unité d’affichage à confirmer

Source Unity · ` data.unity3d::resources.assets ` · PathID 2787

## <img class="stat-icon" src="../public-assets/stats/94dbc9f7dab76bc073a82be3ec13fd9fb1bfb5829ef12728858457fb62a978ac.png" alt="" loading="lazy"> Chance de Gel { #stat-299172729 }

Identifiant · ` 299172729 `

**Description du jeu** · Augmente les chances d’infliger le Gel en touchant un ennemi, réduisant sa vitesse de déplacement\.

**Unité** · Pourcentage (fraction sérialisée)

- Calcul de la chance de gel · ` (GetStat(source,299172729)*(1+GetStat(source,1897309765))) ` · PathID 16585
  - source · ` 299172729 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat-299172729"><img class="stat-icon" src="../public-assets/stats/94dbc9f7dab76bc073a82be3ec13fd9fb1bfb5829ef12728858457fb62a978ac.png" alt="" loading="lazy"> Chance de Gel</a>
  - source · ` 1897309765 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat-1897309765"><img class="stat-icon" src="../public-assets/stats/94dbc9f7dab76bc073a82be3ec13fd9fb1bfb5829ef12728858457fb62a978ac.png" alt="" loading="lazy"> Chance de Gel (%)</a>

Source Unity · ` Stat_Description_ChillChance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16455

## <img class="stat-icon" src="../public-assets/stats/94dbc9f7dab76bc073a82be3ec13fd9fb1bfb5829ef12728858457fb62a978ac.png" alt="" loading="lazy"> Chance de Gel &#40;%&#41; { #stat-1897309765 }

Identifiant · ` 1897309765 `

**Description du jeu** · Augmente les chances d’infliger le Gel en touchant un ennemi, réduisant sa vitesse de déplacement\.

**Unité** · Pourcentage (fraction sérialisée)

- Calcul de la chance de gel · ` (GetStat(source,299172729)*(1+GetStat(source,1897309765))) ` · PathID 16585
  - source · ` 299172729 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat-299172729"><img class="stat-icon" src="../public-assets/stats/94dbc9f7dab76bc073a82be3ec13fd9fb1bfb5829ef12728858457fb62a978ac.png" alt="" loading="lazy"> Chance de Gel</a>
  - source · ` 1897309765 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat-1897309765"><img class="stat-icon" src="../public-assets/stats/94dbc9f7dab76bc073a82be3ec13fd9fb1bfb5829ef12728858457fb62a978ac.png" alt="" loading="lazy"> Chance de Gel (%)</a>

Source Unity · ` Stat_Description_ChillChance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16454

## <img class="stat-icon" src="../public-assets/stats/226c10fc139c5e977f60d4160ecf83440f7d171ccc7146348009dc952ddb9567.png" alt="" loading="lazy"> Chance de Poison { #stat-1687477670 }

Identifiant · ` 1687477670 `

**Description du jeu** · Augmente les chances d’infliger du Poison en touchant un ennemi, infligeant des dégâts sur la durée\.

**Unité** · Pourcentage (fraction sérialisée)

Source Unity · ` Stat_Description_PoisonChance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16502

## <img class="stat-icon" src="../public-assets/stats/226c10fc139c5e977f60d4160ecf83440f7d171ccc7146348009dc952ddb9567.png" alt="" loading="lazy"> Chance de Poison &#40;%&#41; { #stat-1955502493 }

Identifiant · ` 1955502493 `

**Description du jeu** · Augmente les chances d’infliger du Poison en touchant un ennemi, infligeant des dégâts sur la durée\.

**Unité** · Pourcentage (fraction sérialisée)

Source Unity · ` Stat_Description_PoisonChance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16501

## <img class="stat-icon" src="../public-assets/stats/18c10c8af9967e0adce32abab3a23d7d33f495aba12195a580a6999e3b1b51eb.png" alt="" loading="lazy"> Chance de Saignement { #stat--721622672 }

Identifiant · ` -721622672 `

**Description du jeu** · Influence la probabilité d’infliger l’altération Saignement en touchant des ennemis\.

**Unité** · Pourcentage (fraction sérialisée)

Source Unity · ` Stat_Description_BleedChance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16449

## <img class="stat-icon" src="../public-assets/stats/18c10c8af9967e0adce32abab3a23d7d33f495aba12195a580a6999e3b1b51eb.png" alt="" loading="lazy"> Chance de Saignement &#40;%&#41; { #stat-1370990497 }

Identifiant · ` 1370990497 `

**Description du jeu** · Influence la probabilité d’infliger l’altération Saignement en touchant des ennemis\.

**Unité** · Pourcentage (fraction sérialisée)

Source Unity · ` Stat_Description_BleedChance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16448

## <img class="stat-icon" src="../public-assets/stats/cbe94b3a1f79adef805b779ebda03dfcd90ffb8731f72ebb32b01e526f51b27c.png" alt="" loading="lazy"> Cumul de Brûlure { #stat-336023121 }

Identifiant · ` 336023121 `

**Description du jeu** · Détermine le nombre maximal de cumuls de Brûlure pouvant être infligés\.

**Unité** · Unité d’affichage à confirmer

Source Unity · ` Stat_Description_IgniteStack ` · ` data.unity3d::sharedassets0.assets ` · PathID 16477

## <img class="stat-icon" src="../public-assets/stats/900c8f3ed8c40ffb1a072a6670469edb4401dd457273b5824d0c9f75f7df904d.png" alt="" loading="lazy"> Cumul de Choc { #stat-1056975688 }

Identifiant · ` 1056975688 `

**Description du jeu** · Détermine le nombre maximal de cumuls de Choc pouvant être infligés\.

**Unité** · Unité d’affichage à confirmer

Source Unity · ` Stat_Description_ShockStack ` · ` data.unity3d::sharedassets0.assets ` · PathID 16514

## <img class="stat-icon" src="../public-assets/stats/34b7235c822b991afa7ece4aaa169e71c95ad26ac83ef8ce13e9337d7e020cff.png" alt="" loading="lazy"> Cumul de Gel { #stat--1898973418 }

Identifiant · ` -1898973418 `

**Description du jeu** · Détermine le nombre maximal de cumuls de Gel pouvant être infligés\.

**Unité** · Unité d’affichage à confirmer

Source Unity · ` Stat_Description_ChillingStack ` · ` data.unity3d::sharedassets0.assets ` · PathID 16456

## <img class="stat-icon" src="../public-assets/stats/f9006a324fb3346835414732ee6bd8c0d351663697c132abe4d4b0b3fae7f0eb.png" alt="" loading="lazy"> Cumul de Poison { #stat-1748677144 }

Identifiant · ` 1748677144 `

**Description du jeu** · Détermine le nombre maximal de cumuls de Poison pouvant être infligés\.

**Unité** · Unité d’affichage à confirmer

Source Unity · ` Stat_Description_PoisonStack ` · ` data.unity3d::sharedassets0.assets ` · PathID 16504

## <img class="stat-icon" src="../public-assets/stats/65a6ce3b134b812b05ee10a901c55307ca21059579ed12f733a3f532bd4e117b.png" alt="" loading="lazy"> Cumul de Saignement { #stat-810479287 }

Identifiant · ` 810479287 `

**Description du jeu** · Détermine le nombre maximal de cumuls de Saignement pouvant être infligés\.

**Unité** · Unité d’affichage à confirmer

Source Unity · ` Stat_Description_BleedingStack ` · ` data.unity3d::sharedassets0.assets ` · PathID 16450

## <img class="stat-icon" src="../public-assets/stats/4b64f2c2fc9d02b9d36a1f432e4905a8b021aef5180e3423e69b3dbaf41b17f6.png" alt="" loading="lazy"> Dégâts critiques { #stat-1402126566 }

Identifiant · ` 1402126566 `

Fonctionnement précis à confirmer.

**Unité** · Unité d’affichage à confirmer

Source Unity · ` data.unity3d::resources.assets ` · PathID 2788

## <img class="stat-icon" src="../public-assets/stats/0d1f55d63169e7287be71fd637aa74af704ad45d0f327d9508f6e88dfca2e1cb.png" alt="" loading="lazy"> Dégâts de Feu { #stat-1196196874 }

Identifiant · ` 1196196874 `

**Description du jeu** · Affecte le montant des dégâts de feu infligés par tes compétences\.

**Unité** · Unité d’affichage à confirmer

Source Unity · ` Stat_Description_FireDamage ` · ` data.unity3d::sharedassets0.assets ` · PathID 16469

## <img class="stat-icon" src="../public-assets/stats/0d1f55d63169e7287be71fd637aa74af704ad45d0f327d9508f6e88dfca2e1cb.png" alt="" loading="lazy"> Dégâts de Feu &#40;%&#41; { #stat--1666217071 }

Identifiant · ` -1666217071 `

**Description du jeu** · Affecte le montant des dégâts de feu infligés par tes compétences\.

**Unité** · Pourcentage (fraction sérialisée)

Source Unity · ` Stat_Description_FireDamage ` · ` data.unity3d::sharedassets0.assets ` · PathID 16467

## <img class="stat-icon" src="../public-assets/stats/b3b24a21013b8526c326481f082183e3d52ea265d14e46d7f0c73b2a5c91d867.png" alt="" loading="lazy"> Dégâts de Foudre { #stat-217526346 }

Identifiant · ` 217526346 `

**Description du jeu** · Affecte le montant des dégâts de foudre infligés par tes compétences\.

**Unité** · Unité d’affichage à confirmer

Source Unity · ` Stat_Description_LightningDamage ` · ` data.unity3d::sharedassets0.assets ` · PathID 16484

## <img class="stat-icon" src="../public-assets/stats/b3b24a21013b8526c326481f082183e3d52ea265d14e46d7f0c73b2a5c91d867.png" alt="" loading="lazy"> Dégâts de Foudre &#40;%&#41; { #stat--1439315223 }

Identifiant · ` -1439315223 `

**Description du jeu** · Affecte le montant des dégâts de foudre infligés par tes compétences\.

**Unité** · Pourcentage (fraction sérialisée)

Source Unity · ` Stat_Description_LightningDamage ` · ` data.unity3d::sharedassets0.assets ` · PathID 16482

## <img class="stat-icon" src="../public-assets/stats/aca7991fa5e73bacaa21dc8dd32d0d432887fa33e639c5523211db6cc514ab5f.png" alt="" loading="lazy"> Dégâts de Froid { #stat-2056331723 }

Identifiant · ` 2056331723 `

**Description du jeu** · Affecte le montant des dégâts de froid infligés par tes compétences\.

**Unité** · Unité d’affichage à confirmer

- Calcul des dégâts de froid · ` (GetStat(source,2056331723)*(1+GetStat(source,562078803))*GetStat(source,-1015916763)*(1-GetStat(target,1932233781))) ` · PathID 16556
  - source · ` -1015916763 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat--1015916763"><img class="stat-icon" src="../public-assets/stats/ce3c9110b789b436e8dcbdf0361bb0c8fa99537c51f0496316f0e504d2c4f28e.png" alt="" loading="lazy"> Multiplicateur de dégâts de froid</a>
  - source · ` 562078803 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat-562078803"><img class="stat-icon" src="../public-assets/stats/aca7991fa5e73bacaa21dc8dd32d0d432887fa33e639c5523211db6cc514ab5f.png" alt="" loading="lazy"> Dégâts de Froid (%)</a>
  - source · ` 2056331723 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat-2056331723"><img class="stat-icon" src="../public-assets/stats/aca7991fa5e73bacaa21dc8dd32d0d432887fa33e639c5523211db6cc514ab5f.png" alt="" loading="lazy"> Dégâts de Froid</a>
  - cible · ` 1932233781 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat-1932233781"><img class="stat-icon" src="../public-assets/stats/ee2184517ae4fd276a247cac66a7d98bd34c95fc7d65285bc278748967a32d2a.png" alt="" loading="lazy"> Résistance au Froid (%)</a>

Source Unity · ` Stat_Description_ColdDamage ` · ` data.unity3d::sharedassets0.assets ` · PathID 16459

## <img class="stat-icon" src="../public-assets/stats/aca7991fa5e73bacaa21dc8dd32d0d432887fa33e639c5523211db6cc514ab5f.png" alt="" loading="lazy"> Dégâts de Froid &#40;%&#41; { #stat-562078803 }

Identifiant · ` 562078803 `

**Description du jeu** · Affecte le montant des dégâts de froid infligés par tes compétences\.

**Unité** · Pourcentage (fraction sérialisée)

- Calcul des dégâts de froid · ` (GetStat(source,2056331723)*(1+GetStat(source,562078803))*GetStat(source,-1015916763)*(1-GetStat(target,1932233781))) ` · PathID 16556
  - source · ` -1015916763 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat--1015916763"><img class="stat-icon" src="../public-assets/stats/ce3c9110b789b436e8dcbdf0361bb0c8fa99537c51f0496316f0e504d2c4f28e.png" alt="" loading="lazy"> Multiplicateur de dégâts de froid</a>
  - source · ` 562078803 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat-562078803"><img class="stat-icon" src="../public-assets/stats/aca7991fa5e73bacaa21dc8dd32d0d432887fa33e639c5523211db6cc514ab5f.png" alt="" loading="lazy"> Dégâts de Froid (%)</a>
  - source · ` 2056331723 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat-2056331723"><img class="stat-icon" src="../public-assets/stats/aca7991fa5e73bacaa21dc8dd32d0d432887fa33e639c5523211db6cc514ab5f.png" alt="" loading="lazy"> Dégâts de Froid</a>
  - cible · ` 1932233781 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat-1932233781"><img class="stat-icon" src="../public-assets/stats/ee2184517ae4fd276a247cac66a7d98bd34c95fc7d65285bc278748967a32d2a.png" alt="" loading="lazy"> Résistance au Froid (%)</a>

Source Unity · ` Stat_Description_ColdDamage ` · ` data.unity3d::sharedassets0.assets ` · PathID 16457

## <img class="stat-icon" src="../public-assets/stats/b6e7fda8aecd0888e67ddd2be44483293a30df9991a46817ea71533bfab7aae9.png" alt="" loading="lazy"> Dégâts de zone &#40;%&#41; { #stat-2003266556 }

Identifiant · ` 2003266556 `

**Description du jeu** · Détermine les dégâts infligés par les compétences de zone\.

**Unité** · Pourcentage (fraction sérialisée)

Source Unity · ` Stat_Description_AoeDamage ` · ` data.unity3d::sharedassets0.assets ` · PathID 16441

## <img class="stat-icon" src="../public-assets/stats/1bd93df45ed7c71e0c9e9f89ceba4ec764d4a96afcaeb57efc59a131ade027cf.png" alt="" loading="lazy"> Dégâts Physiques { #stat--1329040019 }

Identifiant · ` -1329040019 `

**Description du jeu** · Affecte le montant des dégâts physiques infligés par tes compétences\.

**Unité** · Unité d’affichage à confirmer

Source Unity · ` Stat_Description_PhysicalDamage ` · ` data.unity3d::sharedassets0.assets ` · PathID 16496

## <img class="stat-icon" src="../public-assets/stats/1bd93df45ed7c71e0c9e9f89ceba4ec764d4a96afcaeb57efc59a131ade027cf.png" alt="" loading="lazy"> Dégâts Physiques &#40;%&#41; { #stat-375307812 }

Identifiant · ` 375307812 `

**Description du jeu** · Affecte le montant des dégâts physiques infligés par tes compétences\.

**Unité** · Pourcentage (fraction sérialisée)

Source Unity · ` Stat_Description_PhysicalDamage ` · ` data.unity3d::sharedassets0.assets ` · PathID 16494

## <img class="stat-icon" src="../public-assets/stats/bcb1cacbf09319998699cc874d7a4b4bd212322a707fdc4e7c9b3f5cabb0e1c8.png" alt="" loading="lazy"> Dégâts sur la Durée &#40;%&#41; { #stat-2006839466 }

Identifiant · ` 2006839466 `

**Description du jeu** · Influence les dégâts sur la durée infligés par tes altérations\.

**Unité** · Pourcentage (fraction sérialisée)

Source Unity · ` Stat_Description_DamageOverTime ` · ` data.unity3d::sharedassets0.assets ` · PathID 16463

## <img class="stat-icon" src="../public-assets/stats/ac65159a3402be815cc98fce02ed6f70d83dbf22bb9c4f580c512b888833115b.png" alt="" loading="lazy"> Dés du Destin { #stat-811283535 }

Identifiant · ` 811283535 `

Fonctionnement précis à confirmer.

**Unité** · Unité d’affichage à confirmer

Source Unity · ` data.unity3d::sharedassets0.assets ` · PathID 16464

## <span class="stat-icon-missing" role="img" aria-label="Icône non vérifiée" title="Icône non vérifiée">◇</span> Diviseur d’expérience { #stat-1969273205 }

Identifiant · ` 1969273205 `

Fonctionnement précis à confirmer.

**Unité** · Unité d’affichage à confirmer

Source Unity · ` data.unity3d::sharedassets0.assets ` · PathID 16518

## <img class="stat-icon" src="../public-assets/stats/754ee6e7b29ece2a6010beca144a42e4527f892b68130e851aac03dd25f01656.png" alt="" loading="lazy"> Durée des Altérations { #stat--23940553 }

Identifiant · ` -23940553 `

**Description du jeu** · Affecte la durée des altérations infligées aux ennemis\.

**Unité** · Unité d’affichage à confirmer

- Durée de l’altération · ` (GetStat(source,-23940553)*(1+GetStat(source,-132752378))) ` · PathID 16590
  - source · ` -132752378 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat--132752378"><img class="stat-icon" src="../public-assets/stats/754ee6e7b29ece2a6010beca144a42e4527f892b68130e851aac03dd25f01656.png" alt="" loading="lazy"> Durée des Altérations (%)</a>
  - source · ` -23940553 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat--23940553"><img class="stat-icon" src="../public-assets/stats/754ee6e7b29ece2a6010beca144a42e4527f892b68130e851aac03dd25f01656.png" alt="" loading="lazy"> Durée des Altérations</a>

Source Unity · ` Stat_Description_AilmentDuration ` · ` data.unity3d::sharedassets0.assets ` · PathID 16446

## <img class="stat-icon" src="../public-assets/stats/754ee6e7b29ece2a6010beca144a42e4527f892b68130e851aac03dd25f01656.png" alt="" loading="lazy"> Durée des Altérations &#40;%&#41; { #stat--132752378 }

Identifiant · ` -132752378 `

**Description du jeu** · Affecte la durée des altérations infligées aux ennemis\.

**Unité** · Pourcentage (fraction sérialisée)

- Durée de l’altération · ` (GetStat(source,-23940553)*(1+GetStat(source,-132752378))) ` · PathID 16590
  - source · ` -132752378 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat--132752378"><img class="stat-icon" src="../public-assets/stats/754ee6e7b29ece2a6010beca144a42e4527f892b68130e851aac03dd25f01656.png" alt="" loading="lazy"> Durée des Altérations (%)</a>
  - source · ` -23940553 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat--23940553"><img class="stat-icon" src="../public-assets/stats/754ee6e7b29ece2a6010beca144a42e4527f892b68130e851aac03dd25f01656.png" alt="" loading="lazy"> Durée des Altérations</a>

Source Unity · ` Stat_Description_AilmentDuration ` · ` data.unity3d::sharedassets0.assets ` · PathID 16445

## <img class="stat-icon" src="../public-assets/stats/08b283c173ddeee4d0c9da754febd02c1f119216a91506d9b67faef2c285c77f.png" alt="" loading="lazy"> Durée des Compétences { #stat--1774871374 }

Identifiant · ` -1774871374 `

**Description du jeu** · Influence la durée de tes compétences\.

**Unité** · Unité d’affichage à confirmer

- Durée du projectile · ` (GetStat(source,-1774871374)*(1+GetStat(source,980309249))) ` · PathID 16593
  - source · ` -1774871374 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat--1774871374"><img class="stat-icon" src="../public-assets/stats/08b283c173ddeee4d0c9da754febd02c1f119216a91506d9b67faef2c285c77f.png" alt="" loading="lazy"> Durée des Compétences</a>
  - source · ` 980309249 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat-980309249"><img class="stat-icon" src="../public-assets/stats/08b283c173ddeee4d0c9da754febd02c1f119216a91506d9b67faef2c285c77f.png" alt="" loading="lazy"> Durée des Compétences (%)</a>

Source Unity · ` Stat_Description_Duration ` · ` data.unity3d::sharedassets0.assets ` · PathID 16466

## <img class="stat-icon" src="../public-assets/stats/08b283c173ddeee4d0c9da754febd02c1f119216a91506d9b67faef2c285c77f.png" alt="" loading="lazy"> Durée des Compétences &#40;%&#41; { #stat-980309249 }

Identifiant · ` 980309249 `

**Description du jeu** · Influence la durée de tes compétences\.

**Unité** · Pourcentage (fraction sérialisée)

- Durée du projectile · ` (GetStat(source,-1774871374)*(1+GetStat(source,980309249))) ` · PathID 16593
  - source · ` -1774871374 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat--1774871374"><img class="stat-icon" src="../public-assets/stats/08b283c173ddeee4d0c9da754febd02c1f119216a91506d9b67faef2c285c77f.png" alt="" loading="lazy"> Durée des Compétences</a>
  - source · ` 980309249 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat-980309249"><img class="stat-icon" src="../public-assets/stats/08b283c173ddeee4d0c9da754febd02c1f119216a91506d9b67faef2c285c77f.png" alt="" loading="lazy"> Durée des Compétences (%)</a>

Source Unity · ` Stat_Description_Duration ` · ` data.unity3d::sharedassets0.assets ` · PathID 16465

## <img class="stat-icon" src="../public-assets/stats/5f55e84dbbd3444c80e7805b4abd66700c8925fbe4b9e19cbfb5593928eaab97.png" alt="" loading="lazy"> Efficacité des Soins &#40;%&#41; { #stat-897582809 }

Identifiant · ` 897582809 `

**Description du jeu** · Affecte la puissance des effets de soins de tes compétences\.

**Unité** · Pourcentage (fraction sérialisée)

Source Unity · ` Stat_Description_HealEfficiency ` · ` data.unity3d::sharedassets0.assets ` · PathID 16472

## <img class="stat-icon" src="../public-assets/stats/394adb4d8c89269756e96865d48aeb6df2c6441ecafef74a1128dad49492c7c4.png" alt="" loading="lazy"> Efficacité du Vol de Vie &#40;%&#41; { #stat--1459590084 }

Identifiant · ` -1459590084 `

**Description du jeu** · Régén \+0,125 PV par élimination normale et \+2,5 PV par élimination d'Élite\. Une efficacité plus élevée augmente les PV gagnés par élimination\.

**Unité** · Pourcentage (fraction sérialisée)

Source Unity · ` Stat_Description_LifeSteal ` · ` data.unity3d::sharedassets0.assets ` · PathID 16481

## <img class="stat-icon" src="../public-assets/stats/226e54ad60c0d21105ca530196b45c4362ff0f78e3e04530a0b5de33d602305c.png" alt="" loading="lazy"> Épines { #stat--1417792752 }

Identifiant · ` -1417792752 `

Fonctionnement précis à confirmer.

**Unité** · Unité d’affichage à confirmer

Source Unity · ` data.unity3d::resources.assets ` · PathID 2793

## <span class="stat-icon-missing" role="img" aria-label="Icône non vérifiée" title="Icône non vérifiée">◇</span> Force du bouclier { #stat-1712048563 }

Identifiant · ` 1712048563 `

Fonctionnement précis à confirmer.

**Unité** · Unité d’affichage à confirmer

Source Unity · ` data.unity3d::resources.assets ` · PathID 2791

## <img class="stat-icon" src="../public-assets/stats/f17c43774188f3760887e4ce81d540faed564f2bbd7a089e65484a6ed535f763.png" alt="" loading="lazy"> Gain d’Expérience &#40;%&#41; { #stat-1729853715 }

Identifiant · ` 1729853715 `

Fonctionnement précis à confirmer.

**Unité** · Pourcentage (fraction sérialisée)

Source Unity · ` data.unity3d::sharedassets0.assets ` · PathID 16519

## <span class="stat-icon-missing" role="img" aria-label="Icône non vérifiée" title="Icône non vérifiée">◇</span> Intervalle de décroissance du sursoin { #stat-1910202604 }

Identifiant · ` 1910202604 `

Fonctionnement précis à confirmer.

**Unité** · Unité d’affichage à confirmer

Source Unity · ` data.unity3d::sharedassets0.assets ` · PathID 16493

## <img class="stat-icon" src="../public-assets/stats/12f7a329164a64393bdb39c95bb8e1314fc63b91e297d51fbb25a797396fd9af.png" alt="" loading="lazy"> Multiplicateur de dégâts de feu { #stat-1011286929 }

Identifiant · ` 1011286929 `

**Description du jeu** · Multiplie le montant des dégâts de feu infligés\.

**Unité** · Unité d’affichage à confirmer

Source Unity · ` Stat_Description_FirePenetration ` · ` data.unity3d::sharedassets0.assets ` · PathID 16468

## <img class="stat-icon" src="../public-assets/stats/0913cd8af7b48e2af720fd9e2f5c0f50a75fa3c31ba26ce9993f40411f111239.png" alt="" loading="lazy"> Multiplicateur de dégâts de foudre { #stat-289068898 }

Identifiant · ` 289068898 `

**Description du jeu** · Multiplie le montant des dégâts de foudre infligés\.

**Unité** · Unité d’affichage à confirmer

Source Unity · ` Stat_Description_LightningPenetration ` · ` data.unity3d::sharedassets0.assets ` · PathID 16483

## <img class="stat-icon" src="../public-assets/stats/ce3c9110b789b436e8dcbdf0361bb0c8fa99537c51f0496316f0e504d2c4f28e.png" alt="" loading="lazy"> Multiplicateur de dégâts de froid { #stat--1015916763 }

Identifiant · ` -1015916763 `

**Description du jeu** · Multiplie le montant des dégâts de froid infligés\.

**Unité** · Unité d’affichage à confirmer

- Calcul des dégâts de froid · ` (GetStat(source,2056331723)*(1+GetStat(source,562078803))*GetStat(source,-1015916763)*(1-GetStat(target,1932233781))) ` · PathID 16556
  - source · ` -1015916763 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat--1015916763"><img class="stat-icon" src="../public-assets/stats/ce3c9110b789b436e8dcbdf0361bb0c8fa99537c51f0496316f0e504d2c4f28e.png" alt="" loading="lazy"> Multiplicateur de dégâts de froid</a>
  - source · ` 562078803 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat-562078803"><img class="stat-icon" src="../public-assets/stats/aca7991fa5e73bacaa21dc8dd32d0d432887fa33e639c5523211db6cc514ab5f.png" alt="" loading="lazy"> Dégâts de Froid (%)</a>
  - source · ` 2056331723 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat-2056331723"><img class="stat-icon" src="../public-assets/stats/aca7991fa5e73bacaa21dc8dd32d0d432887fa33e639c5523211db6cc514ab5f.png" alt="" loading="lazy"> Dégâts de Froid</a>
  - cible · ` 1932233781 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat-1932233781"><img class="stat-icon" src="../public-assets/stats/ee2184517ae4fd276a247cac66a7d98bd34c95fc7d65285bc278748967a32d2a.png" alt="" loading="lazy"> Résistance au Froid (%)</a>

Source Unity · ` Stat_Description_ColdPenetration ` · ` data.unity3d::sharedassets0.assets ` · PathID 16458

## <img class="stat-icon" src="../public-assets/stats/49dbfb3210993e59d01e58fc82f602b2f8c9185a631bd03f6b9c8d9ef67540bf.png" alt="" loading="lazy"> Multiplicateur de dégâts physiques { #stat-1240293936 }

Identifiant · ` 1240293936 `

**Description du jeu** · Multiplie le montant des dégâts physiques infligés\.

**Unité** · Unité d’affichage à confirmer

Source Unity · ` Stat_Description_PhysicalPenetration ` · ` data.unity3d::sharedassets0.assets ` · PathID 16495

## <span class="stat-icon-missing" role="img" aria-label="Icône non vérifiée" title="Icône non vérifiée">◇</span> Multiplicateur des récompenses de salle { #stat--1031067952 }

Identifiant · ` -1031067952 `

Fonctionnement précis à confirmer.

**Unité** · Unité d’affichage à confirmer

Source Unity · ` data.unity3d::resources.assets ` · PathID 2790

## <img class="stat-icon" src="../public-assets/stats/a04d6a231ebace6118785b3159979a27a3e2302d4498e4002639530d29e97956.png" alt="" loading="lazy"> Munitions { #stat-2068885608 }

Identifiant · ` 2068885608 `

Fonctionnement précis à confirmer.

**Unité** · Unité d’affichage à confirmer

Source Unity · ` data.unity3d::resources.assets ` · PathID 2786

## <span class="stat-icon-missing" role="img" aria-label="Icône non vérifiée" title="Icône non vérifiée">◇</span> Niveau { #stat--412912059 }

Identifiant · ` -412912059 `

Fonctionnement précis à confirmer.

**Unité** · Unité d’affichage à confirmer

Source Unity · ` data.unity3d::sharedassets0.assets ` · PathID 16480

## <img class="stat-icon" src="../public-assets/stats/b84826196b02bd72c949e89271fc22078cac98935e47069884cf1830203aafca.png" alt="" loading="lazy"> Nombre de Projectiles { #stat--530233839 }

Identifiant · ` -530233839 `

**Description du jeu** · Nombre de projectiles supplémentaires ajoutés à tes compétences\.

**Unité** · Nombre

- Nombre de projectiles · ` GetStat(source,-530233839) ` · PathID 16596
  - source · ` -530233839 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat--530233839"><img class="stat-icon" src="../public-assets/stats/b84826196b02bd72c949e89271fc22078cac98935e47069884cf1830203aafca.png" alt="" loading="lazy"> Nombre de Projectiles</a>

Source Unity · ` Stat_Description_ProjectileCount ` · ` data.unity3d::sharedassets0.assets ` · PathID 16507

## <img class="stat-icon" src="../public-assets/stats/1ceeb0e531bcc028361a4a8be837f255fc3181842626853370b927d6a38d96c4.png" alt="" loading="lazy"> Nombre de Ricochets { #stat-444703137 }

Identifiant · ` 444703137 `

**Description du jeu** · Détermine combien de fois une compétence peut ricocher entre des ennemis, frappant et appliquant des effets à plusieurs cibles en sautant de l’une à l’autre\.

**Unité** · Nombre

Source Unity · ` Stat_Description_ChainCount ` · ` data.unity3d::sharedassets0.assets ` · PathID 16452

## <img class="stat-icon" src="../public-assets/stats/a9921fbc069c2af458c7ea27422672504aed1ac0014c70701298472598686183.png" alt="" loading="lazy"> Nombre de Transpercements { #stat-530049776 }

Identifiant · ` 530049776 `

**Description du jeu** · Détermine combien de fois une compétence peut transpercer des ennemis, les frappant et appliquant des effets à d’autres cibles sans être détruite\.

**Unité** · Unité d’affichage à confirmer

Source Unity · ` Stat_Description_PierceCount ` · ` data.unity3d::sharedassets0.assets ` · PathID 16508

## <span class="stat-icon-missing" role="img" aria-label="Icône non vérifiée" title="Icône non vérifiée">◇</span> Perte de sursoin { #stat-1910202603 }

Identifiant · ` 1910202603 `

Fonctionnement précis à confirmer.

**Unité** · Unité d’affichage à confirmer

Source Unity · ` data.unity3d::sharedassets0.assets ` · PathID 16492

## <img class="stat-icon" src="../public-assets/stats/8634a9b53a54481dc9558adcaad82ad1914921856f7f0cd910951d750c32e608.png" alt="" loading="lazy"> Points d’endurance maximum { #stat--412042601 }

Identifiant · ` -412042601 `

Fonctionnement précis à confirmer.

**Unité** · Unité d’affichage à confirmer

Source Unity · ` data.unity3d::sharedassets0.assets ` · PathID 16516

## <img class="stat-icon" src="../public-assets/stats/d8399cf543dad2ac547e79901fa86e52c996e818a9a5b93a42252d5f00d7c123.png" alt="" loading="lazy"> Portée de Ramassage { #stat--1969582225 }

Identifiant · ` -1969582225 `

**Description du jeu** · Détermine la portée à laquelle tu peux ramasser des objets ou des orbes\.

**Unité** · Unité d’affichage à confirmer

Source Unity · ` Stat_Description_PickupRange ` · ` data.unity3d::sharedassets0.assets ` · PathID 16500

## <img class="stat-icon" src="../public-assets/stats/d8399cf543dad2ac547e79901fa86e52c996e818a9a5b93a42252d5f00d7c123.png" alt="" loading="lazy"> Portée de Ramassage &#40;%&#41; { #stat--1920634750 }

Identifiant · ` -1920634750 `

**Description du jeu** · Détermine la portée à laquelle tu peux ramasser des objets ou des orbes\.

**Unité** · Pourcentage (fraction sérialisée)

Source Unity · ` Stat_Description_PickupRange ` · ` data.unity3d::sharedassets0.assets ` · PathID 16499

## <img class="stat-icon" src="../public-assets/stats/87fbb7ba47316145974811d99c45bc8fffc1430c07695f967bdfc89940291436.png" alt="" loading="lazy"> Portée de Ricochet { #stat-1362684812 }

Identifiant · ` 1362684812 `

**Description du jeu** · Influence la distance qu’une compétence peut parcourir en ricochant entre des ennemis\.

**Unité** · Unité d’affichage à confirmer

Source Unity · ` Stat_Description_ChainDistance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16506

## <img class="stat-icon" src="../public-assets/stats/87fbb7ba47316145974811d99c45bc8fffc1430c07695f967bdfc89940291436.png" alt="" loading="lazy"> Portée de Ricochet &#40;%&#41; { #stat--1677646303 }

Identifiant · ` -1677646303 `

**Description du jeu** · Influence la distance qu’une compétence peut parcourir en ricochant entre des ennemis\.

**Unité** · Pourcentage (fraction sérialisée)

Source Unity · ` Stat_Description_ChainDistance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16505

## <img class="stat-icon" src="../public-assets/stats/46380b849c8bde17107567500a31a8e5dc61eed2f6612c3cb9d435f831cb7778.png" alt="" loading="lazy"> Puissance de Brûlure { #stat--1598137134 }

Identifiant · ` -1598137134 `

**Description du jeu** · L’effet de Brûlure est plus efficace\. Inflige plus de dégâts sur la durée\.

**Unité** · Unité d’affichage à confirmer

Source Unity · ` Stat_Description_IgnitePower ` · ` data.unity3d::sharedassets0.assets ` · PathID 16474

## <img class="stat-icon" src="../public-assets/stats/6c5c4151344f56aa64b965b888c1079b3382c2c3a9595f0a057122ae5f5943e2.png" alt="" loading="lazy"> Puissance de Choc { #stat-2069118412 }

Identifiant · ` 2069118412 `

**Description du jeu** · L’effet de Choc est plus efficace\. Multiplie davantage les dégâts\.

**Unité** · Unité d’affichage à confirmer

Source Unity · ` Stat_Description_ShockPower ` · ` data.unity3d::sharedassets0.assets ` · PathID 16511

## <img class="stat-icon" src="../public-assets/stats/cfd6385d5ae0d3893d3bd22097eb59c0e2bea8a2e0d4cb78969ecfd5e362cf81.png" alt="" loading="lazy"> Puissance de Gel { #stat--1475948281 }

Identifiant · ` -1475948281 `

**Description du jeu** · L’effet de Givre est plus efficace\. Applique un ralentissement plus puissant\.

**Unité** · Unité d’affichage à confirmer

Source Unity · ` Stat_Description_ChillingPower ` · ` data.unity3d::sharedassets0.assets ` · PathID 16453

## <img class="stat-icon" src="../public-assets/stats/453b4c1ccc9d36079814657db8ecfeba99e2a3c62c4995365fc53df7e8de513d.png" alt="" loading="lazy"> Puissance de Poison { #stat-62229812 }

Identifiant · ` 62229812 `

**Description du jeu** · L’effet du Poison est plus efficace\. Il inflige encore plus de dégâts\.

**Unité** · Unité d’affichage à confirmer

Source Unity · ` Stat_Description_PoisonPower ` · ` data.unity3d::sharedassets0.assets ` · PathID 16503

## <img class="stat-icon" src="../public-assets/stats/79b632a73c6e92286075c8e9b8f5d5c66c706d780db2d537fee62019dea652c4.png" alt="" loading="lazy"> Puissance de Saignement { #stat--595531990 }

Identifiant · ` -595531990 `

**Description du jeu** · L’effet de Saignement est plus efficace\. Inflige plus de dégâts sur la durée\.

**Unité** · Unité d’affichage à confirmer

Source Unity · ` Stat_Description_BleedingPower ` · ` data.unity3d::sharedassets0.assets ` · PathID 16447

## <img class="stat-icon" src="../public-assets/stats/3b81dea6160b385bae6ca408eec4122d539d8cf1f32e370156f80e2de3003324.png" alt="" loading="lazy"> Qualité de l’Expérience &#40;%&#41; { #stat-1605897117 }

Identifiant · ` 1605897117 `

Fonctionnement précis à confirmer.

**Unité** · Pourcentage (fraction sérialisée)

Source Unity · ` data.unity3d::sharedassets0.assets ` · PathID 16520

## <span class="stat-icon-missing" role="img" aria-label="Icône non vérifiée" title="Icône non vérifiée">◇</span> Quantité de sursoin perdue &#40;%&#41; { #stat-1111063864 }

Identifiant · ` 1111063864 `

Fonctionnement précis à confirmer.

**Unité** · Pourcentage (fraction sérialisée)

Source Unity · ` data.unity3d::resources.assets ` · PathID 2789

## <img class="stat-icon" src="../public-assets/stats/36c3eeae8ed160c547de1d6b9aa6c1e98807e5270e99c4b773a94d77dd38c215.png" alt="" loading="lazy"> Quantité d’Objets &#40;%&#41; { #stat-2045188474 }

Identifiant · ` 2045188474 `

Fonctionnement précis à confirmer.

**Unité** · Pourcentage (fraction sérialisée)

Source Unity · ` data.unity3d::sharedassets0.assets ` · PathID 16478

## <img class="stat-icon" src="../public-assets/stats/e0d52f26b70888964a0fe9722d40497e4e509b10e78ed14e3ec8fd8f92638d2a.png" alt="" loading="lazy"> Rareté des Cartes &#40;%&#41; { #stat-536066167 }

Identifiant · ` 536066167 `

Fonctionnement précis à confirmer.

**Unité** · Pourcentage (fraction sérialisée)

Source Unity · ` data.unity3d::sharedassets0.assets ` · PathID 16451

## <img class="stat-icon" src="../public-assets/stats/d5d1ae9af9f21456d4c3a6c6eff56af91422edb515371f4ed7181a8de4539290.png" alt="" loading="lazy"> Rareté des Objets &#40;%&#41; { #stat--155820065 }

Identifiant · ` -155820065 `

Fonctionnement précis à confirmer.

**Unité** · Pourcentage (fraction sérialisée)

Source Unity · ` data.unity3d::sharedassets0.assets ` · PathID 16479

## <img class="stat-icon" src="../public-assets/stats/08b283c173ddeee4d0c9da754febd02c1f119216a91506d9b67faef2c285c77f.png" alt="" loading="lazy"> Recharge { #stat--1565260718 }

Identifiant · ` -1565260718 `

Valeur de recharge lue par la formule de Boule de Givre.

**Unité** · Unité d’affichage à confirmer

- Calcul de la recharge · ` (GetStat(source,-1565260718)/(1+GetStat(source,-858402365))) ` · PathID 16592
  - source · ` -1565260718 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat--1565260718"><img class="stat-icon" src="../public-assets/stats/08b283c173ddeee4d0c9da754febd02c1f119216a91506d9b67faef2c285c77f.png" alt="" loading="lazy"> Recharge</a>
  - source · ` -858402365 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat--858402365"><img class="stat-icon" src="../public-assets/stats/3d1b8135c0792796b6d5d9016c5f2633b1d6b574aef42b684f3f2d461f0b6706.png" alt="" loading="lazy"> Accélération des Compétences (%)</a>

Source Unity · ` data.unity3d::sharedassets0.assets ` · PathID 16462

## <img class="stat-icon" src="../public-assets/stats/8634a9b53a54481dc9558adcaad82ad1914921856f7f0cd910951d750c32e608.png" alt="" loading="lazy"> Recharge de l’endurance { #stat-830812871 }

Identifiant · ` 830812871 `

Fonctionnement précis à confirmer.

**Unité** · Unité d’affichage à confirmer

Source Unity · ` data.unity3d::sharedassets0.assets ` · PathID 16515

## <img class="stat-icon" src="../public-assets/stats/1f48bc83460ad779d7eb5ef27d793a5c247381d7a32faf2157ec33793172b0e0.png" alt="" loading="lazy"> Résistance au Feu &#40;%&#41; { #stat-1645300642 }

Identifiant · ` 1645300642 `

**Description du jeu** · Détermine ta résistance aux dégâts de feu, subissant moins de dégâts\.

**Unité** · Pourcentage (fraction sérialisée)

Source Unity · ` Stat_Description_FireResistance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16471

## <img class="stat-icon" src="../public-assets/stats/ee2184517ae4fd276a247cac66a7d98bd34c95fc7d65285bc278748967a32d2a.png" alt="" loading="lazy"> Résistance au Froid &#40;%&#41; { #stat-1932233781 }

Identifiant · ` 1932233781 `

**Description du jeu** · Détermine ta résistance aux dégâts de froid, subissant moins de dégâts\.

**Unité** · Pourcentage (fraction sérialisée)

- Calcul des dégâts de froid · ` (GetStat(source,2056331723)*(1+GetStat(source,562078803))*GetStat(source,-1015916763)*(1-GetStat(target,1932233781))) ` · PathID 16556
  - source · ` -1015916763 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat--1015916763"><img class="stat-icon" src="../public-assets/stats/ce3c9110b789b436e8dcbdf0361bb0c8fa99537c51f0496316f0e504d2c4f28e.png" alt="" loading="lazy"> Multiplicateur de dégâts de froid</a>
  - source · ` 562078803 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat-562078803"><img class="stat-icon" src="../public-assets/stats/aca7991fa5e73bacaa21dc8dd32d0d432887fa33e639c5523211db6cc514ab5f.png" alt="" loading="lazy"> Dégâts de Froid (%)</a>
  - source · ` 2056331723 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat-2056331723"><img class="stat-icon" src="../public-assets/stats/aca7991fa5e73bacaa21dc8dd32d0d432887fa33e639c5523211db6cc514ab5f.png" alt="" loading="lazy"> Dégâts de Froid</a>
  - cible · ` 1932233781 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat-1932233781"><img class="stat-icon" src="../public-assets/stats/ee2184517ae4fd276a247cac66a7d98bd34c95fc7d65285bc278748967a32d2a.png" alt="" loading="lazy"> Résistance au Froid (%)</a>

Source Unity · ` Stat_Description_ColdResistance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16461

## <img class="stat-icon" src="../public-assets/stats/dbe1f970860c6d3afa9a0ff92fd3ed835e3cdefc63f35b307a706f1ff138aef0.png" alt="" loading="lazy"> Résistance aux ralentissements { #stat--1844310897 }

Identifiant · ` -1844310897 `

**Description du jeu** · La Ténacité réduit l'impact des ralentissements et divers effets de contrôle

**Unité** · Unité d’affichage à confirmer

Source Unity · ` Stat_Description_Tenacity ` · ` data.unity3d::sharedassets0.assets ` · PathID 16517

## <img class="stat-icon" src="../public-assets/stats/2f154db037264ffc504eac411a4bfbe99fa9344e6d8f12ba91aeb16d72529b4c.png" alt="" loading="lazy"> Résistance à la Foudre &#40;%&#41; { #stat-153888567 }

Identifiant · ` 153888567 `

**Description du jeu** · Détermine ta résistance aux dégâts de foudre, subissant moins de dégâts\.

**Unité** · Pourcentage (fraction sérialisée)

Source Unity · ` Stat_Description_LightningResistance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16486

## <img class="stat-icon" src="../public-assets/stats/4c1ebc5c7e6a1039e8b0a5a7303824c47334a32941b2294b9e71b9d7eec0c97c.png" alt="" loading="lazy"> Résistance Maximale au Feu &#40;%&#41; { #stat-122110380 }

Identifiant · ` 122110380 `

**Description du jeu** · Détermine ta résistance maximale au feu\.

**Unité** · Pourcentage (fraction sérialisée)

Source Unity · ` Stat_Description_MaximumFireResistance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16470

## <img class="stat-icon" src="../public-assets/stats/9ae54565e58a291e21412929bb9bb4a3ddbaf62ea393e6c6690ba6a162039b46.png" alt="" loading="lazy"> Résistance Maximale au Froid &#40;%&#41; { #stat-1562786720 }

Identifiant · ` 1562786720 `

**Description du jeu** · Détermine ta résistance maximale au froid\.

**Unité** · Pourcentage (fraction sérialisée)

Source Unity · ` Stat_Description_MaximumColdResistance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16460

## <img class="stat-icon" src="../public-assets/stats/72e5a6c8393faa7a4bc9b16c044bf89c173fb90df6c8f9856c38092ddd7fb6f6.png" alt="" loading="lazy"> Résistance Maximale à la Foudre &#40;%&#41; { #stat--1582074329 }

Identifiant · ` -1582074329 `

**Description du jeu** · Détermine ta résistance maximale à la foudre\.

**Unité** · Pourcentage (fraction sérialisée)

Source Unity · ` Stat_Description_MaximumLightningResistance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16485

## <img class="stat-icon" src="../public-assets/stats/a7c44f74fd336c64853e8177389480e0374244f22f7994f4982bf396d5cc7b24.png" alt="" loading="lazy"> Résistance Physique &#40;%&#41; { #stat-2137905250 }

Identifiant · ` 2137905250 `

**Description du jeu** · Détermine ta résistance aux dégâts physiques, subissant moins de dégâts\.

**Unité** · Pourcentage (fraction sérialisée)

Source Unity · ` Stat_Description_PhysicalResistance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16498

## <img class="stat-icon" src="../public-assets/stats/1c88b0f5346520409c78e50bcef3fd3d9bcc93eed97130c64241a17045ca66c8.png" alt="" loading="lazy"> Résistance Physique Maximale &#40;%&#41; { #stat-1220215810 }

Identifiant · ` 1220215810 `

**Description du jeu** · Détermine ta résistance physique maximale\.

**Unité** · Pourcentage (fraction sérialisée)

Source Unity · ` Stat_Description_MaximumPhysicalResistance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16497

## <img class="stat-icon" src="../public-assets/stats/8634a9b53a54481dc9558adcaad82ad1914921856f7f0cd910951d750c32e608.png" alt="" loading="lazy"> Taux de récupération de l’endurance &#40;%&#41; { #stat--485591111 }

Identifiant · ` -485591111 `

Fonctionnement précis à confirmer.

**Unité** · Pourcentage (fraction sérialisée)

Source Unity · ` data.unity3d::resources.assets ` · PathID 2792

## <img class="stat-icon" src="../public-assets/stats/77ad6d4d1d06e8ca413100020bc8421b25572094d91285bf096a85106b919330.png" alt="" loading="lazy"> Vie Augmentée &#40;%&#41; { #stat-529736145 }

Identifiant · ` 529736145 `

**Description du jeu** · Détermine ta santé maximale\.

**Unité** · Pourcentage (fraction sérialisée)

Source Unity · ` Stat_Description_Maxhealth ` · ` data.unity3d::sharedassets0.assets ` · PathID 16487

## <img class="stat-icon" src="../public-assets/stats/77ad6d4d1d06e8ca413100020bc8421b25572094d91285bf096a85106b919330.png" alt="" loading="lazy"> Vie Brute { #stat-71032185 }

Identifiant · ` 71032185 `

**Description du jeu** · Détermine ta santé maximale\.

**Unité** · Unité d’affichage à confirmer

Source Unity · ` Stat_Description_Maxhealth ` · ` data.unity3d::sharedassets0.assets ` · PathID 16488

## <img class="stat-icon" src="../public-assets/stats/5f55e84dbbd3444c80e7805b4abd66700c8925fbe4b9e19cbfb5593928eaab97.png" alt="" loading="lazy"> Vie récupérée par incantation { #stat--537215961 }

Identifiant · ` -537215961 `

**Description du jeu** · Affecte la puissance des effets de soins de tes compétences\.

**Unité** · Unité d’affichage à confirmer

Source Unity · ` Stat_Description_HealEfficiency ` · ` data.unity3d::sharedassets0.assets ` · PathID 16473

## <img class="stat-icon" src="../public-assets/stats/855423c4aa13c2b6b239a05a81cbf6e7d778b297dc166cf01f217da04fffff02.png" alt="" loading="lazy"> Vitesse de Déplacement { #stat-411658539 }

Identifiant · ` 411658539 `

Fonctionnement précis à confirmer.

**Unité** · Unité d’affichage à confirmer

Source Unity · ` data.unity3d::sharedassets0.assets ` · PathID 16490

## <img class="stat-icon" src="../public-assets/stats/855423c4aa13c2b6b239a05a81cbf6e7d778b297dc166cf01f217da04fffff02.png" alt="" loading="lazy"> Vitesse de Déplacement &#40;%&#41; { #stat--1427501575 }

Identifiant · ` -1427501575 `

**Description du jeu** · Influence ta vitesse de déplacement\.

**Unité** · Pourcentage (fraction sérialisée)

Source Unity · ` Stat_Description_MovementSpeed ` · ` data.unity3d::sharedassets0.assets ` · PathID 16489

## <img class="stat-icon" src="../public-assets/stats/9b2665345ce216ed4466bffc743727b3dc39e750b20c8f611c3b11eaf1865dc1.png" alt="" loading="lazy"> Vitesse des Projectiles { #stat-631551606 }

Identifiant · ` 631551606 `

**Description du jeu** · Modifie la vitesse de tes projectiles\.

**Unité** · Unité d’affichage à confirmer

- Vitesse du projectile · ` (GetStat(source,631551606)*(1+GetStat(source,1250534698))) ` · PathID 16598
  - source · ` 631551606 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat-631551606"><img class="stat-icon" src="../public-assets/stats/9b2665345ce216ed4466bffc743727b3dc39e750b20c8f611c3b11eaf1865dc1.png" alt="" loading="lazy"> Vitesse des Projectiles</a>
  - source · ` 1250534698 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat-1250534698"><img class="stat-icon" src="../public-assets/stats/9b2665345ce216ed4466bffc743727b3dc39e750b20c8f611c3b11eaf1865dc1.png" alt="" loading="lazy"> Vitesse des Projectiles (%)</a>

Source Unity · ` Stat_Description_ProjectileSpeed ` · ` data.unity3d::sharedassets0.assets ` · PathID 16510

## <img class="stat-icon" src="../public-assets/stats/9b2665345ce216ed4466bffc743727b3dc39e750b20c8f611c3b11eaf1865dc1.png" alt="" loading="lazy"> Vitesse des Projectiles &#40;%&#41; { #stat-1250534698 }

Identifiant · ` 1250534698 `

**Description du jeu** · Modifie la vitesse de tes projectiles\.

**Unité** · Pourcentage (fraction sérialisée)

- Vitesse du projectile · ` (GetStat(source,631551606)*(1+GetStat(source,1250534698))) ` · PathID 16598
  - source · ` 631551606 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat-631551606"><img class="stat-icon" src="../public-assets/stats/9b2665345ce216ed4466bffc743727b3dc39e750b20c8f611c3b11eaf1865dc1.png" alt="" loading="lazy"> Vitesse des Projectiles</a>
  - source · ` 1250534698 ` · <a class="stat-reference" href="@wiki/caracteristiques/#stat-1250534698"><img class="stat-icon" src="../public-assets/stats/9b2665345ce216ed4466bffc743727b3dc39e750b20c8f611c3b11eaf1865dc1.png" alt="" loading="lazy"> Vitesse des Projectiles (%)</a>

Source Unity · ` Stat_Description_ProjectileSpeed ` · ` data.unity3d::sharedassets0.assets ` · PathID 16509

## <img class="stat-icon" src="../public-assets/stats/73d930f8590bf10ea6ad1166695376f19b2a77f08f4ec71597c661bb18af00d3.png" alt="" loading="lazy"> Zone d’Effet { #stat-1017502194 }

Identifiant · ` 1017502194 `

**Description du jeu** · Influence la zone d’effet de tes compétences\.

**Unité** · Unité d’affichage à confirmer

Source Unity · ` Stat_Description_AreaOfEffect ` · ` data.unity3d::sharedassets0.assets ` · PathID 16443

## <img class="stat-icon" src="../public-assets/stats/73d930f8590bf10ea6ad1166695376f19b2a77f08f4ec71597c661bb18af00d3.png" alt="" loading="lazy"> Zone d’Effet &#40;%&#41; { #stat--581418117 }

Identifiant · ` -581418117 `

**Description du jeu** · Influence la zone d’effet de tes compétences\.

**Unité** · Pourcentage (fraction sérialisée)

Source Unity · ` Stat_Description_AreaOfEffect ` · ` data.unity3d::sharedassets0.assets ` · PathID 16442
