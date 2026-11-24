# Stats

Game descriptions state the intended role. The formulas below are verified serialized expressions. Each note states what has been verified for the build under review.

<a href="@alternate/">Français</a>

## <img class="stat-icon" src="../public-assets/stats/08b283c173ddeee4d0c9da754febd02c1f119216a91506d9b67faef2c285c77f.png" alt="" loading="lazy"> Ability Duration { #stat--1774871374 }

ID · ` -1774871374 `

**Game description** · Influences the duration of your abilities\.

**Unit** · Display unit unconfirmed

<div class="wiki-formula"><p class="formula-title">Projectile lifetime <small>· PathID 16593</small></p><p class="formula-expression">(<a class="stat-reference" href="@wiki/stats/#stat--1774871374"><img class="stat-icon" src="../public-assets/stats/08b283c173ddeee4d0c9da754febd02c1f119216a91506d9b67faef2c285c77f.png" alt="" loading="lazy"> Ability Duration <small class="formula-scope">(source)</small></a> × <wbr>(1 + <wbr><a class="stat-reference" href="@wiki/stats/#stat-980309249"><img class="stat-icon" src="../public-assets/stats/08b283c173ddeee4d0c9da754febd02c1f119216a91506d9b67faef2c285c77f.png" alt="" loading="lazy"> Ability Duration (%) <small class="formula-scope">(source)</small></a>))</p><details class="formula-source"><summary>Original Unity formula</summary><pre><code>(GetStat(source,-1774871374)*(1+GetStat(source,980309249)))</code></pre><p>Unity · <code>data.unity3d::sharedassets0.assets</code> · PathID 16593</p><p><code>_data / _formula · offset 64</code></p></details></div>

Source Unity · ` Stat_Description_Duration ` · ` data.unity3d::sharedassets0.assets ` · PathID 16466

## <img class="stat-icon" src="../public-assets/stats/08b283c173ddeee4d0c9da754febd02c1f119216a91506d9b67faef2c285c77f.png" alt="" loading="lazy"> Ability Duration &#40;%&#41; { #stat-980309249 }

ID · ` 980309249 `

**Game description** · Influences the duration of your abilities\.

**Unit** · Percentage (serialized fraction)

<div class="wiki-formula"><p class="formula-title">Projectile lifetime <small>· PathID 16593</small></p><p class="formula-expression">(<a class="stat-reference" href="@wiki/stats/#stat--1774871374"><img class="stat-icon" src="../public-assets/stats/08b283c173ddeee4d0c9da754febd02c1f119216a91506d9b67faef2c285c77f.png" alt="" loading="lazy"> Ability Duration <small class="formula-scope">(source)</small></a> × <wbr>(1 + <wbr><a class="stat-reference" href="@wiki/stats/#stat-980309249"><img class="stat-icon" src="../public-assets/stats/08b283c173ddeee4d0c9da754febd02c1f119216a91506d9b67faef2c285c77f.png" alt="" loading="lazy"> Ability Duration (%) <small class="formula-scope">(source)</small></a>))</p><details class="formula-source"><summary>Original Unity formula</summary><pre><code>(GetStat(source,-1774871374)*(1+GetStat(source,980309249)))</code></pre><p>Unity · <code>data.unity3d::sharedassets0.assets</code> · PathID 16593</p><p><code>_data / _formula · offset 64</code></p></details></div>

Source Unity · ` Stat_Description_Duration ` · ` data.unity3d::sharedassets0.assets ` · PathID 16465

## <img class="stat-icon" src="../public-assets/stats/3d1b8135c0792796b6d5d9016c5f2633b1d6b574aef42b684f3f2d461f0b6706.png" alt="" loading="lazy"> Ability Haste &#40;%&#41; { #stat--858402365 }

ID · ` -858402365 `

**Game description** · Influences the cooldown of your abilities, for every 100 Ability Haste, cooldowns are halved\.

**Unit** · Percentage (serialized fraction)

<div class="wiki-formula"><p class="formula-title">Cooldown calculation <small>· PathID 16592</small></p><p class="formula-expression">(<a class="stat-reference" href="@wiki/stats/#stat--1565260718"><img class="stat-icon" src="../public-assets/stats/08b283c173ddeee4d0c9da754febd02c1f119216a91506d9b67faef2c285c77f.png" alt="" loading="lazy"> Cooldown <small class="formula-scope">(source)</small></a> / <wbr>(1 + <wbr><a class="stat-reference" href="@wiki/stats/#stat--858402365"><img class="stat-icon" src="../public-assets/stats/3d1b8135c0792796b6d5d9016c5f2633b1d6b574aef42b684f3f2d461f0b6706.png" alt="" loading="lazy"> Ability Haste (%) <small class="formula-scope">(source)</small></a>))</p><details class="formula-source"><summary>Original Unity formula</summary><pre><code>(GetStat(source,-1565260718)/(1+GetStat(source,-858402365)))</code></pre><p>Unity · <code>data.unity3d::sharedassets0.assets</code> · PathID 16592</p><p><code>_data / _formula · offset 64</code></p></details></div>

Source Unity · ` Stat_Description_AbilityHaste ` · ` data.unity3d::sharedassets0.assets ` · PathID 16444

## <img class="stat-icon" src="../public-assets/stats/754ee6e7b29ece2a6010beca144a42e4527f892b68130e851aac03dd25f01656.png" alt="" loading="lazy"> Ailment Duration { #stat--23940553 }

ID · ` -23940553 `

**Game description** · Affects the duration of ailments inflicted on enemies\.

**Unit** · Display unit unconfirmed

<div class="wiki-formula"><p class="formula-title">Ailment duration <small>· PathID 16590</small></p><p class="formula-expression">(<a class="stat-reference" href="@wiki/stats/#stat--23940553"><img class="stat-icon" src="../public-assets/stats/754ee6e7b29ece2a6010beca144a42e4527f892b68130e851aac03dd25f01656.png" alt="" loading="lazy"> Ailment Duration <small class="formula-scope">(source)</small></a> × <wbr>(1 + <wbr><a class="stat-reference" href="@wiki/stats/#stat--132752378"><img class="stat-icon" src="../public-assets/stats/754ee6e7b29ece2a6010beca144a42e4527f892b68130e851aac03dd25f01656.png" alt="" loading="lazy"> Ailment Duration (%) <small class="formula-scope">(source)</small></a>))</p><details class="formula-source"><summary>Original Unity formula</summary><pre><code>(GetStat(source,-23940553)*(1+GetStat(source,-132752378)))</code></pre><p>Unity · <code>data.unity3d::sharedassets0.assets</code> · PathID 16590</p><p><code>_data / _formula · offset 72</code></p></details></div>

Source Unity · ` Stat_Description_AilmentDuration ` · ` data.unity3d::sharedassets0.assets ` · PathID 16446

## <img class="stat-icon" src="../public-assets/stats/754ee6e7b29ece2a6010beca144a42e4527f892b68130e851aac03dd25f01656.png" alt="" loading="lazy"> Ailment Duration &#40;%&#41; { #stat--132752378 }

ID · ` -132752378 `

**Game description** · Affects the duration of ailments inflicted on enemies\.

**Unit** · Percentage (serialized fraction)

<div class="wiki-formula"><p class="formula-title">Ailment duration <small>· PathID 16590</small></p><p class="formula-expression">(<a class="stat-reference" href="@wiki/stats/#stat--23940553"><img class="stat-icon" src="../public-assets/stats/754ee6e7b29ece2a6010beca144a42e4527f892b68130e851aac03dd25f01656.png" alt="" loading="lazy"> Ailment Duration <small class="formula-scope">(source)</small></a> × <wbr>(1 + <wbr><a class="stat-reference" href="@wiki/stats/#stat--132752378"><img class="stat-icon" src="../public-assets/stats/754ee6e7b29ece2a6010beca144a42e4527f892b68130e851aac03dd25f01656.png" alt="" loading="lazy"> Ailment Duration (%) <small class="formula-scope">(source)</small></a>))</p><details class="formula-source"><summary>Original Unity formula</summary><pre><code>(GetStat(source,-23940553)*(1+GetStat(source,-132752378)))</code></pre><p>Unity · <code>data.unity3d::sharedassets0.assets</code> · PathID 16590</p><p><code>_data / _formula · offset 72</code></p></details></div>

Source Unity · ` Stat_Description_AilmentDuration ` · ` data.unity3d::sharedassets0.assets ` · PathID 16445

## <img class="stat-icon" src="../public-assets/stats/a04d6a231ebace6118785b3159979a27a3e2302d4498e4002639530d29e97956.png" alt="" loading="lazy"> Ammunition { #stat-2068885608 }

ID · ` 2068885608 `

**Unit** · Display unit unconfirmed

Exact behaviour remains unconfirmed.

Source Unity · ` data.unity3d::resources.assets ` · PathID 2786

## <img class="stat-icon" src="../public-assets/stats/73d930f8590bf10ea6ad1166695376f19b2a77f08f4ec71597c661bb18af00d3.png" alt="" loading="lazy"> Area of Effect { #stat-1017502194 }

ID · ` 1017502194 `

**Game description** · Influences the area of effect of your abilities\.

**Unit** · Display unit unconfirmed

Source Unity · ` Stat_Description_AreaOfEffect ` · ` data.unity3d::sharedassets0.assets ` · PathID 16443

## <img class="stat-icon" src="../public-assets/stats/73d930f8590bf10ea6ad1166695376f19b2a77f08f4ec71597c661bb18af00d3.png" alt="" loading="lazy"> Area of Effect &#40;%&#41; { #stat--581418117 }

ID · ` -581418117 `

**Game description** · Influences the area of effect of your abilities\.

**Unit** · Percentage (serialized fraction)

Source Unity · ` Stat_Description_AreaOfEffect ` · ` data.unity3d::sharedassets0.assets ` · PathID 16442

## <img class="stat-icon" src="../public-assets/stats/b6e7fda8aecd0888e67ddd2be44483293a30df9991a46817ea71533bfab7aae9.png" alt="" loading="lazy"> Area Of Effect Damage &#40;%&#41; { #stat-2003266556 }

ID · ` 2003266556 `

**Game description** · Determines the damage dealt by area\-of\-effect abilities\.

**Unit** · Percentage (serialized fraction)

Source Unity · ` Stat_Description_AoeDamage ` · ` data.unity3d::sharedassets0.assets ` · PathID 16441

## <img class="stat-icon" src="../public-assets/stats/18c10c8af9967e0adce32abab3a23d7d33f495aba12195a580a6999e3b1b51eb.png" alt="" loading="lazy"> Bleed Chance { #stat--721622672 }

ID · ` -721622672 `

**Game description** · Influences the chance to inflict the Bleeding ailment upon hitting enemies\.

**Unit** · Percentage (serialized fraction)

Source Unity · ` Stat_Description_BleedChance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16449

## <img class="stat-icon" src="../public-assets/stats/18c10c8af9967e0adce32abab3a23d7d33f495aba12195a580a6999e3b1b51eb.png" alt="" loading="lazy"> Bleed Chance &#40;%&#41; { #stat-1370990497 }

ID · ` 1370990497 `

**Game description** · Influences the chance to inflict the Bleeding ailment upon hitting enemies\.

**Unit** · Percentage (serialized fraction)

Source Unity · ` Stat_Description_BleedChance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16448

## <img class="stat-icon" src="../public-assets/stats/79b632a73c6e92286075c8e9b8f5d5c66c706d780db2d537fee62019dea652c4.png" alt="" loading="lazy"> Bleed Power { #stat--595531990 }

ID · ` -595531990 `

**Game description** · The effect of Bleeding is more effective\. Deals more damage over time\.

**Unit** · Display unit unconfirmed

Source Unity · ` Stat_Description_BleedingPower ` · ` data.unity3d::sharedassets0.assets ` · PathID 16447

## <img class="stat-icon" src="../public-assets/stats/65a6ce3b134b812b05ee10a901c55307ca21059579ed12f733a3f532bd4e117b.png" alt="" loading="lazy"> Bleed Stack { #stat-810479287 }

ID · ` 810479287 `

**Game description** · Determines the maximum number of Bleeding stacks that can be inflicted\.

**Unit** · Display unit unconfirmed

Source Unity · ` Stat_Description_BleedingStack ` · ` data.unity3d::sharedassets0.assets ` · PathID 16450

## <img class="stat-icon" src="../public-assets/stats/e0d52f26b70888964a0fe9722d40497e4e509b10e78ed14e3ec8fd8f92638d2a.png" alt="" loading="lazy"> Card Rarity &#40;%&#41; { #stat-536066167 }

ID · ` 536066167 `

**Game description** · When drawing cards, they are favorably rerolled, and the highest possible rarity is kept\.

**Unit** · Percentage (serialized fraction)

Exact behaviour remains unconfirmed.

Source Unity · ` Stat_Description_CardRarity ` · ` data.unity3d::sharedassets0.assets ` · PathID 16451

## <img class="stat-icon" src="../public-assets/stats/1ceeb0e531bcc028361a4a8be837f255fc3181842626853370b927d6a38d96c4.png" alt="" loading="lazy"> Chain Count { #stat-444703137 }

ID · ` 444703137 `

**Game description** · Determines how many times an ability can chain between enemies, striking and applying effects to multiple targets as it leaps from one to the next\.

**Unit** · Count

Source Unity · ` Stat_Description_ChainCount ` · ` data.unity3d::sharedassets0.assets ` · PathID 16452

## <img class="stat-icon" src="../public-assets/stats/87fbb7ba47316145974811d99c45bc8fffc1430c07695f967bdfc89940291436.png" alt="" loading="lazy"> Chain Distance { #stat-1362684812 }

ID · ` 1362684812 `

**Game description** · Influences the distance an ability can travel while chaining between enemies\.

**Unit** · Display unit unconfirmed

Source Unity · ` Stat_Description_ChainDistance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16506

## <img class="stat-icon" src="../public-assets/stats/87fbb7ba47316145974811d99c45bc8fffc1430c07695f967bdfc89940291436.png" alt="" loading="lazy"> Chain Distance &#40;%&#41; { #stat--1677646303 }

ID · ` -1677646303 `

**Game description** · Influences the distance an ability can travel while chaining between enemies\.

**Unit** · Percentage (serialized fraction)

Source Unity · ` Stat_Description_ChainDistance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16505

## <img class="stat-icon" src="../public-assets/stats/94dbc9f7dab76bc073a82be3ec13fd9fb1bfb5829ef12728858457fb62a978ac.png" alt="" loading="lazy"> Chill Chance { #stat-299172729 }

ID · ` 299172729 `

**Game description** · Increases the chance to inflict Chilling on hitting an enemy, reducing their movement speed\.

**Unit** · Percentage (serialized fraction)

<div class="wiki-formula"><p class="formula-title">Chilling chance calculation <small>· PathID 16585</small></p><p class="formula-expression">(<a class="stat-reference" href="@wiki/stats/#stat-299172729"><img class="stat-icon" src="../public-assets/stats/94dbc9f7dab76bc073a82be3ec13fd9fb1bfb5829ef12728858457fb62a978ac.png" alt="" loading="lazy"> Chill Chance <small class="formula-scope">(source)</small></a> × <wbr>(1 + <wbr><a class="stat-reference" href="@wiki/stats/#stat-1897309765"><img class="stat-icon" src="../public-assets/stats/94dbc9f7dab76bc073a82be3ec13fd9fb1bfb5829ef12728858457fb62a978ac.png" alt="" loading="lazy"> Chill Chance (%) <small class="formula-scope">(source)</small></a>))</p><details class="formula-source"><summary>Original Unity formula</summary><pre><code>(GetStat(source,299172729)*(1+GetStat(source,1897309765)))</code></pre><p>Unity · <code>data.unity3d::sharedassets0.assets</code> · PathID 16585</p><p><code>_data / _formula · offset 76</code></p></details></div>

Source Unity · ` Stat_Description_ChillChance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16455

## <img class="stat-icon" src="../public-assets/stats/94dbc9f7dab76bc073a82be3ec13fd9fb1bfb5829ef12728858457fb62a978ac.png" alt="" loading="lazy"> Chill Chance &#40;%&#41; { #stat-1897309765 }

ID · ` 1897309765 `

**Game description** · Increases the chance to inflict Chilling on hitting an enemy, reducing their movement speed\.

**Unit** · Percentage (serialized fraction)

<div class="wiki-formula"><p class="formula-title">Chilling chance calculation <small>· PathID 16585</small></p><p class="formula-expression">(<a class="stat-reference" href="@wiki/stats/#stat-299172729"><img class="stat-icon" src="../public-assets/stats/94dbc9f7dab76bc073a82be3ec13fd9fb1bfb5829ef12728858457fb62a978ac.png" alt="" loading="lazy"> Chill Chance <small class="formula-scope">(source)</small></a> × <wbr>(1 + <wbr><a class="stat-reference" href="@wiki/stats/#stat-1897309765"><img class="stat-icon" src="../public-assets/stats/94dbc9f7dab76bc073a82be3ec13fd9fb1bfb5829ef12728858457fb62a978ac.png" alt="" loading="lazy"> Chill Chance (%) <small class="formula-scope">(source)</small></a>))</p><details class="formula-source"><summary>Original Unity formula</summary><pre><code>(GetStat(source,299172729)*(1+GetStat(source,1897309765)))</code></pre><p>Unity · <code>data.unity3d::sharedassets0.assets</code> · PathID 16585</p><p><code>_data / _formula · offset 76</code></p></details></div>

Source Unity · ` Stat_Description_ChillChance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16454

## <img class="stat-icon" src="../public-assets/stats/cfd6385d5ae0d3893d3bd22097eb59c0e2bea8a2e0d4cb78969ecfd5e362cf81.png" alt="" loading="lazy"> Chill Power { #stat--1475948281 }

ID · ` -1475948281 `

**Game description** · The effect of Chilling is more effective\. Applies a stronger slow\.

**Unit** · Display unit unconfirmed

Source Unity · ` Stat_Description_ChillingPower ` · ` data.unity3d::sharedassets0.assets ` · PathID 16453

## <img class="stat-icon" src="../public-assets/stats/34b7235c822b991afa7ece4aaa169e71c95ad26ac83ef8ce13e9337d7e020cff.png" alt="" loading="lazy"> Chill Stack { #stat--1898973418 }

ID · ` -1898973418 `

**Game description** · Determines the maximum number of Chilling stacks that can be inflicted\.

**Unit** · Display unit unconfirmed

Source Unity · ` Stat_Description_ChillingStack ` · ` data.unity3d::sharedassets0.assets ` · PathID 16456

## <img class="stat-icon" src="../public-assets/stats/aca7991fa5e73bacaa21dc8dd32d0d432887fa33e639c5523211db6cc514ab5f.png" alt="" loading="lazy"> Cold Damage { #stat-2056331723 }

ID · ` 2056331723 `

**Game description** · Affects the amount of cold damage dealt by your abilities\.

**Unit** · Display unit unconfirmed

<div class="wiki-formula"><p class="formula-title">Cold damage calculation <small>· PathID 16556</small></p><p class="formula-expression">(<a class="stat-reference" href="@wiki/stats/#stat-2056331723"><img class="stat-icon" src="../public-assets/stats/aca7991fa5e73bacaa21dc8dd32d0d432887fa33e639c5523211db6cc514ab5f.png" alt="" loading="lazy"> Cold Damage <small class="formula-scope">(source)</small></a> × <wbr>(1 + <wbr><a class="stat-reference" href="@wiki/stats/#stat-562078803"><img class="stat-icon" src="../public-assets/stats/aca7991fa5e73bacaa21dc8dd32d0d432887fa33e639c5523211db6cc514ab5f.png" alt="" loading="lazy"> Cold Damage (%) <small class="formula-scope">(source)</small></a>) × <wbr><a class="stat-reference" href="@wiki/stats/#stat--1015916763"><img class="stat-icon" src="../public-assets/stats/ce3c9110b789b436e8dcbdf0361bb0c8fa99537c51f0496316f0e504d2c4f28e.png" alt="" loading="lazy"> Cold Damage Multiplier <small class="formula-scope">(source)</small></a> × <wbr>(1 − <wbr><a class="stat-reference" href="@wiki/stats/#stat-1932233781"><img class="stat-icon" src="../public-assets/stats/ee2184517ae4fd276a247cac66a7d98bd34c95fc7d65285bc278748967a32d2a.png" alt="" loading="lazy"> Cold Resistance (%) <small class="formula-scope">(target)</small></a>))</p><details class="formula-source"><summary>Original Unity formula</summary><pre><code>(GetStat(source,2056331723)*(1+GetStat(source,562078803))*GetStat(source,-1015916763)*(1-GetStat(target,1932233781)))</code></pre><p>Unity · <code>data.unity3d::sharedassets0.assets</code> · PathID 16556</p><p><code>_data / _formula · offset 52</code></p></details></div>

Source Unity · ` Stat_Description_ColdDamage ` · ` data.unity3d::sharedassets0.assets ` · PathID 16459

## <img class="stat-icon" src="../public-assets/stats/aca7991fa5e73bacaa21dc8dd32d0d432887fa33e639c5523211db6cc514ab5f.png" alt="" loading="lazy"> Cold Damage &#40;%&#41; { #stat-562078803 }

ID · ` 562078803 `

**Game description** · Affects the amount of cold damage dealt by your abilities\.

**Unit** · Percentage (serialized fraction)

<div class="wiki-formula"><p class="formula-title">Cold damage calculation <small>· PathID 16556</small></p><p class="formula-expression">(<a class="stat-reference" href="@wiki/stats/#stat-2056331723"><img class="stat-icon" src="../public-assets/stats/aca7991fa5e73bacaa21dc8dd32d0d432887fa33e639c5523211db6cc514ab5f.png" alt="" loading="lazy"> Cold Damage <small class="formula-scope">(source)</small></a> × <wbr>(1 + <wbr><a class="stat-reference" href="@wiki/stats/#stat-562078803"><img class="stat-icon" src="../public-assets/stats/aca7991fa5e73bacaa21dc8dd32d0d432887fa33e639c5523211db6cc514ab5f.png" alt="" loading="lazy"> Cold Damage (%) <small class="formula-scope">(source)</small></a>) × <wbr><a class="stat-reference" href="@wiki/stats/#stat--1015916763"><img class="stat-icon" src="../public-assets/stats/ce3c9110b789b436e8dcbdf0361bb0c8fa99537c51f0496316f0e504d2c4f28e.png" alt="" loading="lazy"> Cold Damage Multiplier <small class="formula-scope">(source)</small></a> × <wbr>(1 − <wbr><a class="stat-reference" href="@wiki/stats/#stat-1932233781"><img class="stat-icon" src="../public-assets/stats/ee2184517ae4fd276a247cac66a7d98bd34c95fc7d65285bc278748967a32d2a.png" alt="" loading="lazy"> Cold Resistance (%) <small class="formula-scope">(target)</small></a>))</p><details class="formula-source"><summary>Original Unity formula</summary><pre><code>(GetStat(source,2056331723)*(1+GetStat(source,562078803))*GetStat(source,-1015916763)*(1-GetStat(target,1932233781)))</code></pre><p>Unity · <code>data.unity3d::sharedassets0.assets</code> · PathID 16556</p><p><code>_data / _formula · offset 52</code></p></details></div>

Source Unity · ` Stat_Description_ColdDamage ` · ` data.unity3d::sharedassets0.assets ` · PathID 16457

## <img class="stat-icon" src="../public-assets/stats/ce3c9110b789b436e8dcbdf0361bb0c8fa99537c51f0496316f0e504d2c4f28e.png" alt="" loading="lazy"> Cold Damage Multiplier { #stat--1015916763 }

ID · ` -1015916763 `

**Game description** · Multiply the amount of Cold damage dealt\.

**Unit** · Display unit unconfirmed

<div class="wiki-formula"><p class="formula-title">Cold damage calculation <small>· PathID 16556</small></p><p class="formula-expression">(<a class="stat-reference" href="@wiki/stats/#stat-2056331723"><img class="stat-icon" src="../public-assets/stats/aca7991fa5e73bacaa21dc8dd32d0d432887fa33e639c5523211db6cc514ab5f.png" alt="" loading="lazy"> Cold Damage <small class="formula-scope">(source)</small></a> × <wbr>(1 + <wbr><a class="stat-reference" href="@wiki/stats/#stat-562078803"><img class="stat-icon" src="../public-assets/stats/aca7991fa5e73bacaa21dc8dd32d0d432887fa33e639c5523211db6cc514ab5f.png" alt="" loading="lazy"> Cold Damage (%) <small class="formula-scope">(source)</small></a>) × <wbr><a class="stat-reference" href="@wiki/stats/#stat--1015916763"><img class="stat-icon" src="../public-assets/stats/ce3c9110b789b436e8dcbdf0361bb0c8fa99537c51f0496316f0e504d2c4f28e.png" alt="" loading="lazy"> Cold Damage Multiplier <small class="formula-scope">(source)</small></a> × <wbr>(1 − <wbr><a class="stat-reference" href="@wiki/stats/#stat-1932233781"><img class="stat-icon" src="../public-assets/stats/ee2184517ae4fd276a247cac66a7d98bd34c95fc7d65285bc278748967a32d2a.png" alt="" loading="lazy"> Cold Resistance (%) <small class="formula-scope">(target)</small></a>))</p><details class="formula-source"><summary>Original Unity formula</summary><pre><code>(GetStat(source,2056331723)*(1+GetStat(source,562078803))*GetStat(source,-1015916763)*(1-GetStat(target,1932233781)))</code></pre><p>Unity · <code>data.unity3d::sharedassets0.assets</code> · PathID 16556</p><p><code>_data / _formula · offset 52</code></p></details></div>

Source Unity · ` Stat_Description_ColdPenetration ` · ` data.unity3d::sharedassets0.assets ` · PathID 16458

## <img class="stat-icon" src="../public-assets/stats/ee2184517ae4fd276a247cac66a7d98bd34c95fc7d65285bc278748967a32d2a.png" alt="" loading="lazy"> Cold Resistance &#40;%&#41; { #stat-1932233781 }

ID · ` 1932233781 `

**Game description** · Determines your resistance to cold damage, taking less damage in the process\.

**Unit** · Percentage (serialized fraction)

<div class="wiki-formula"><p class="formula-title">Cold damage calculation <small>· PathID 16556</small></p><p class="formula-expression">(<a class="stat-reference" href="@wiki/stats/#stat-2056331723"><img class="stat-icon" src="../public-assets/stats/aca7991fa5e73bacaa21dc8dd32d0d432887fa33e639c5523211db6cc514ab5f.png" alt="" loading="lazy"> Cold Damage <small class="formula-scope">(source)</small></a> × <wbr>(1 + <wbr><a class="stat-reference" href="@wiki/stats/#stat-562078803"><img class="stat-icon" src="../public-assets/stats/aca7991fa5e73bacaa21dc8dd32d0d432887fa33e639c5523211db6cc514ab5f.png" alt="" loading="lazy"> Cold Damage (%) <small class="formula-scope">(source)</small></a>) × <wbr><a class="stat-reference" href="@wiki/stats/#stat--1015916763"><img class="stat-icon" src="../public-assets/stats/ce3c9110b789b436e8dcbdf0361bb0c8fa99537c51f0496316f0e504d2c4f28e.png" alt="" loading="lazy"> Cold Damage Multiplier <small class="formula-scope">(source)</small></a> × <wbr>(1 − <wbr><a class="stat-reference" href="@wiki/stats/#stat-1932233781"><img class="stat-icon" src="../public-assets/stats/ee2184517ae4fd276a247cac66a7d98bd34c95fc7d65285bc278748967a32d2a.png" alt="" loading="lazy"> Cold Resistance (%) <small class="formula-scope">(target)</small></a>))</p><details class="formula-source"><summary>Original Unity formula</summary><pre><code>(GetStat(source,2056331723)*(1+GetStat(source,562078803))*GetStat(source,-1015916763)*(1-GetStat(target,1932233781)))</code></pre><p>Unity · <code>data.unity3d::sharedassets0.assets</code> · PathID 16556</p><p><code>_data / _formula · offset 52</code></p></details></div>

Source Unity · ` Stat_Description_ColdResistance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16461

## <img class="stat-icon" src="../public-assets/stats/08b283c173ddeee4d0c9da754febd02c1f119216a91506d9b67faef2c285c77f.png" alt="" loading="lazy"> Cooldown { #stat--1565260718 }

ID · ` -1565260718 `

Cooldown input read by the Frost Ball formula.

**Unit** · Display unit unconfirmed

<div class="wiki-formula"><p class="formula-title">Cooldown calculation <small>· PathID 16592</small></p><p class="formula-expression">(<a class="stat-reference" href="@wiki/stats/#stat--1565260718"><img class="stat-icon" src="../public-assets/stats/08b283c173ddeee4d0c9da754febd02c1f119216a91506d9b67faef2c285c77f.png" alt="" loading="lazy"> Cooldown <small class="formula-scope">(source)</small></a> / <wbr>(1 + <wbr><a class="stat-reference" href="@wiki/stats/#stat--858402365"><img class="stat-icon" src="../public-assets/stats/3d1b8135c0792796b6d5d9016c5f2633b1d6b574aef42b684f3f2d461f0b6706.png" alt="" loading="lazy"> Ability Haste (%) <small class="formula-scope">(source)</small></a>))</p><details class="formula-source"><summary>Original Unity formula</summary><pre><code>(GetStat(source,-1565260718)/(1+GetStat(source,-858402365)))</code></pre><p>Unity · <code>data.unity3d::sharedassets0.assets</code> · PathID 16592</p><p><code>_data / _formula · offset 64</code></p></details></div>

Source Unity · ` data.unity3d::sharedassets0.assets ` · PathID 16462

## <img class="stat-icon" src="../public-assets/stats/67c949ee0937605db9c9fd0295ac69b6e0624a2dd7572fe662ae5954dcd2ccc5.png" alt="" loading="lazy"> Critical chance { #stat-967725324 }

ID · ` 967725324 `

**Unit** · Display unit unconfirmed

Exact behaviour remains unconfirmed.

Source Unity · ` data.unity3d::resources.assets ` · PathID 2787

## <img class="stat-icon" src="../public-assets/stats/4b64f2c2fc9d02b9d36a1f432e4905a8b021aef5180e3423e69b3dbaf41b17f6.png" alt="" loading="lazy"> Critical damage { #stat-1402126566 }

ID · ` 1402126566 `

**Unit** · Display unit unconfirmed

Exact behaviour remains unconfirmed.

Source Unity · ` data.unity3d::resources.assets ` · PathID 2788

## <img class="stat-icon" src="../public-assets/stats/bcb1cacbf09319998699cc874d7a4b4bd212322a707fdc4e7c9b3f5cabb0e1c8.png" alt="" loading="lazy"> Damage Over Time &#40;%&#41; { #stat-2006839466 }

ID · ` 2006839466 `

**Game description** · Influences the damage over time dealt by your ailments\.

**Unit** · Percentage (serialized fraction)

Source Unity · ` Stat_Description_DamageOverTime ` · ` data.unity3d::sharedassets0.assets ` · PathID 16463

## <img class="stat-icon" src="../public-assets/stats/f17c43774188f3760887e4ce81d540faed564f2bbd7a089e65484a6ed535f763.png" alt="" loading="lazy"> Experience Gain &#40;%&#41; { #stat-1729853715 }

ID · ` 1729853715 `

**Game description** · Influences the amount of experience gained when collecting experience orbs\.

**Unit** · Percentage (serialized fraction)

**Observed configuration** · All five ranges on the Experience Gain card and the XpMultiplier relic bonus target this stat\. · ` sharedassets0.assets PathIDs 17338, 19764 `

Exact behaviour remains unconfirmed.

Source Unity · ` Stat_Description_ExperienceGain ` · ` data.unity3d::sharedassets0.assets ` · PathID 16519

## <img class="stat-icon" src="../public-assets/stats/3b81dea6160b385bae6ca408eec4122d539d8cf1f32e370156f80e2de3003324.png" alt="" loading="lazy"> Experience Quality &#40;%&#41; { #stat-1605897117 }

ID · ` 1605897117 `

**Game description** · When experience orbs drop, they are favorably rerolled to ensure the highest possible tier\.

**Unit** · Percentage (serialized fraction)

**Verified code and formula** · Feeds the orb\-quality multiplier in the loot context\. A value of 25% gives a multiplier of 1\.25\.

**Scope of verification** · How the multiplier translates into orb tiers and probabilities remains unconfirmed\.

<div class="wiki-formula"><p class="formula-title">Serialized formula <small>· PathID 16555</small></p><p class="formula-expression">(1 + <wbr><a class="stat-reference" href="@wiki/stats/#stat-1605897117"><img class="stat-icon" src="../public-assets/stats/3b81dea6160b385bae6ca408eec4122d539d8cf1f32e370156f80e2de3003324.png" alt="" loading="lazy"> Experience Quality (%) <small class="formula-scope">(source)</small></a>)</p><details class="formula-source"><summary>Original Unity formula</summary><pre><code>(1+GetStat(source,1605897117))</code></pre><p>Unity · <code>data.unity3d::sharedassets0.assets</code> · PathID 16555</p><p><code>_data / _formula</code></p></details></div>

` ARPGEntity_Module_LootProvider.PopulateContext · RVA 0x880090 · sharedassets0.assets PathID 20433 `

Source Unity · ` Stat_Description_ExperienceQuality ` · ` data.unity3d::sharedassets0.assets ` · PathID 16520

## <img class="stat-icon" src="../public-assets/stats/ac65159a3402be815cc98fce02ed6f70d83dbf22bb9c4f580c512b888833115b.png" alt="" loading="lazy"> Fate Dice { #stat-811283535 }

ID · ` 811283535 `

**Game description** · Currency that can be used to alter card draws in various ways\.

**Unit** · Display unit unconfirmed

**Observed configuration** · The Fate Dice configuration points to this starting stat\. The in\-game balance is a separate attribute\. · ` sharedassets0.assets PathID 19184 · _starterStat, _relatedAttribute `

Exact behaviour remains unconfirmed.

Source Unity · ` Currency_Description_FateDice ` · ` data.unity3d::sharedassets0.assets ` · PathID 16464

## <img class="stat-icon" src="../public-assets/stats/0d1f55d63169e7287be71fd637aa74af704ad45d0f327d9508f6e88dfca2e1cb.png" alt="" loading="lazy"> Fire Damage { #stat-1196196874 }

ID · ` 1196196874 `

**Game description** · Affects the amount of fire damage dealt by your abilities\.

**Unit** · Display unit unconfirmed

Source Unity · ` Stat_Description_FireDamage ` · ` data.unity3d::sharedassets0.assets ` · PathID 16469

## <img class="stat-icon" src="../public-assets/stats/0d1f55d63169e7287be71fd637aa74af704ad45d0f327d9508f6e88dfca2e1cb.png" alt="" loading="lazy"> Fire Damage &#40;%&#41; { #stat--1666217071 }

ID · ` -1666217071 `

**Game description** · Affects the amount of fire damage dealt by your abilities\.

**Unit** · Percentage (serialized fraction)

Source Unity · ` Stat_Description_FireDamage ` · ` data.unity3d::sharedassets0.assets ` · PathID 16467

## <img class="stat-icon" src="../public-assets/stats/12f7a329164a64393bdb39c95bb8e1314fc63b91e297d51fbb25a797396fd9af.png" alt="" loading="lazy"> Fire Damage Multiplier { #stat-1011286929 }

ID · ` 1011286929 `

**Game description** · Multiply the amount of Fire damage dealt\.

**Unit** · Display unit unconfirmed

Source Unity · ` Stat_Description_FirePenetration ` · ` data.unity3d::sharedassets0.assets ` · PathID 16468

## <img class="stat-icon" src="../public-assets/stats/1f48bc83460ad779d7eb5ef27d793a5c247381d7a32faf2157ec33793172b0e0.png" alt="" loading="lazy"> Fire Resistance &#40;%&#41; { #stat-1645300642 }

ID · ` 1645300642 `

**Game description** · Determines your resistance to fire damage, taking less damage in the process\.

**Unit** · Percentage (serialized fraction)

Source Unity · ` Stat_Description_FireResistance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16471

## <img class="stat-icon" src="../public-assets/stats/77ad6d4d1d06e8ca413100020bc8421b25572094d91285bf096a85106b919330.png" alt="" loading="lazy"> Flat Health { #stat-71032185 }

ID · ` 71032185 `

**Game description** · Determines your maximum health\.

**Unit** · Display unit unconfirmed

Source Unity · ` Stat_Description_Maxhealth ` · ` data.unity3d::sharedassets0.assets ` · PathID 16488

## <img class="stat-icon" src="../public-assets/stats/5f55e84dbbd3444c80e7805b4abd66700c8925fbe4b9e19cbfb5593928eaab97.png" alt="" loading="lazy"> Heal Efficiency &#40;%&#41; { #stat-897582809 }

ID · ` 897582809 `

**Game description** · Affects the potency of healing effects from your abilities\.

**Unit** · Percentage (serialized fraction)

Source Unity · ` Stat_Description_HealEfficiency ` · ` data.unity3d::sharedassets0.assets ` · PathID 16472

## <img class="stat-icon" src="../public-assets/stats/5f55e84dbbd3444c80e7805b4abd66700c8925fbe4b9e19cbfb5593928eaab97.png" alt="" loading="lazy"> Health Recovered per Cast { #stat--537215961 }

ID · ` -537215961 `

**Game description** · Affects the potency of healing effects from your abilities\.

**Unit** · Display unit unconfirmed

Source Unity · ` Stat_Description_HealEfficiency ` · ` data.unity3d::sharedassets0.assets ` · PathID 16473

## <img class="stat-icon" src="../public-assets/stats/32d42a9c52e20b9621925a0c55f7d2586294d8f9964338c247a665579ee8d903.png" alt="" loading="lazy"> Ignite Chance { #stat--241968088 }

ID · ` -241968088 `

**Game description** · Increases the chance to inflict Ignite on hitting an enemy, dealing damage over time that scales with the initial hit damage\.

**Unit** · Percentage (serialized fraction)

Source Unity · ` Stat_Description_IgniteChance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16476

## <img class="stat-icon" src="../public-assets/stats/32d42a9c52e20b9621925a0c55f7d2586294d8f9964338c247a665579ee8d903.png" alt="" loading="lazy"> Ignite Chance &#40;%&#41; { #stat--1810387509 }

ID · ` -1810387509 `

**Game description** · Increases the chance to inflict Ignite on hitting an enemy, dealing damage over time that scales with the initial hit damage\.

**Unit** · Percentage (serialized fraction)

Source Unity · ` Stat_Description_IgniteChance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16475

## <img class="stat-icon" src="../public-assets/stats/46380b849c8bde17107567500a31a8e5dc61eed2f6612c3cb9d435f831cb7778.png" alt="" loading="lazy"> Ignite Power { #stat--1598137134 }

ID · ` -1598137134 `

**Game description** · The effect of Ignite is more effective\. Deals more damage over time\.

**Unit** · Display unit unconfirmed

Source Unity · ` Stat_Description_IgnitePower ` · ` data.unity3d::sharedassets0.assets ` · PathID 16474

## <img class="stat-icon" src="../public-assets/stats/cbe94b3a1f79adef805b779ebda03dfcd90ffb8731f72ebb32b01e526f51b27c.png" alt="" loading="lazy"> Ignite Stack { #stat-336023121 }

ID · ` 336023121 `

**Game description** · Determines the maximum number of Ignite stacks that can be inflicted\.

**Unit** · Display unit unconfirmed

Source Unity · ` Stat_Description_IgniteStack ` · ` data.unity3d::sharedassets0.assets ` · PathID 16477

## <img class="stat-icon" src="../public-assets/stats/77ad6d4d1d06e8ca413100020bc8421b25572094d91285bf096a85106b919330.png" alt="" loading="lazy"> Increased Health &#40;%&#41; { #stat-529736145 }

ID · ` 529736145 `

**Game description** · Determines your maximum health\.

**Unit** · Percentage (serialized fraction)

Source Unity · ` Stat_Description_Maxhealth ` · ` data.unity3d::sharedassets0.assets ` · PathID 16487

## <img class="stat-icon" src="../public-assets/stats/36c3eeae8ed160c547de1d6b9aa6c1e98807e5270e99c4b773a94d77dd38c215.png" alt="" loading="lazy"> Item Quantity &#40;%&#41; { #stat-2045188474 }

ID · ` 2045188474 `

**Game description** · Influences the amount of items dropped from foes or chests\.

**Unit** · Percentage (serialized fraction)

**Verified code and formula** · Feeds the quantity multiplier in the loot context\. A value of 25% gives a multiplier of 1\.25\.

**Scope of verification** · Rounding and which loot tables are affected remain unconfirmed\.

<div class="wiki-formula"><p class="formula-title">Serialized formula <small>· PathID 16553</small></p><p class="formula-expression">(1 + <wbr><a class="stat-reference" href="@wiki/stats/#stat-2045188474"><img class="stat-icon" src="../public-assets/stats/36c3eeae8ed160c547de1d6b9aa6c1e98807e5270e99c4b773a94d77dd38c215.png" alt="" loading="lazy"> Item Quantity (%) <small class="formula-scope">(source)</small></a>)</p><details class="formula-source"><summary>Original Unity formula</summary><pre><code>(1+GetStat(source,2045188474))</code></pre><p>Unity · <code>data.unity3d::sharedassets0.assets</code> · PathID 16553</p><p><code>_data / _formula</code></p></details></div>

` ARPGEntity_Module_LootProvider.PopulateContext · RVA 0x880090 · sharedassets0.assets PathID 20433 `

Source Unity · ` Stat_Description_ItemQuantity ` · ` data.unity3d::sharedassets0.assets ` · PathID 16478

## <img class="stat-icon" src="../public-assets/stats/d5d1ae9af9f21456d4c3a6c6eff56af91422edb515371f4ed7181a8de4539290.png" alt="" loading="lazy"> Item Rarity &#40;%&#41; { #stat--155820065 }

ID · ` -155820065 `

**Game description** · When items drop, they are favorably rerolled, and the highest possible rarity is retained\.

**Unit** · Percentage (serialized fraction)

**Verified code and formula** · Feeds the rarity multiplier in the loot context\. A value of 25% gives a multiplier of 1\.25\.

**Scope of verification** · How the multiplier translates into rerolls and probabilities remains unconfirmed\.

<div class="wiki-formula"><p class="formula-title">Serialized formula <small>· PathID 16554</small></p><p class="formula-expression">(1 + <wbr><a class="stat-reference" href="@wiki/stats/#stat--155820065"><img class="stat-icon" src="../public-assets/stats/d5d1ae9af9f21456d4c3a6c6eff56af91422edb515371f4ed7181a8de4539290.png" alt="" loading="lazy"> Item Rarity (%) <small class="formula-scope">(source)</small></a>)</p><details class="formula-source"><summary>Original Unity formula</summary><pre><code>(1+GetStat(source,-155820065))</code></pre><p>Unity · <code>data.unity3d::sharedassets0.assets</code> · PathID 16554</p><p><code>_data / _formula</code></p></details></div>

` ARPGEntity_Module_LootProvider.PopulateContext · RVA 0x880090 · sharedassets0.assets PathID 20433 `

Source Unity · ` Stat_Description_ItemRarity ` · ` data.unity3d::sharedassets0.assets ` · PathID 16479

## <span class="stat-icon-missing" role="img" aria-label="Icon unverified" title="Icon unverified">◇</span> Level { #stat--412912059 }

ID · ` -412912059 `

**Unit** · Integer level

**Behaviour confirmed in code** · The value read by the level module\. The module converts it to an integer by truncating the fractional part\.

**Scope of verification** · Level also feeds the XP attribute maximum\. The progression cap remains unconfirmed\.

<div class="wiki-formula"><p class="formula-title">Serialized formula <small>· PathID 16387</small></p><p class="formula-expression">(((<a class="stat-reference" href="@wiki/stats/#stat--412912059"><span class="stat-icon-missing" role="img" aria-label="Icon unverified" title="Icon unverified">◇</span> Level <small class="formula-scope">(source)</small></a> ^ <wbr>Branch((Branch((<a class="stat-reference" href="@wiki/stats/#stat--412912059"><span class="stat-icon-missing" role="img" aria-label="Icon unverified" title="Icon unverified">◇</span> Level <small class="formula-scope">(source)</small></a> &lt; <wbr>80), <wbr>1.4, <wbr>(1.08 + <wbr>(<a class="stat-reference" href="@wiki/stats/#stat--412912059"><span class="stat-icon-missing" role="img" aria-label="Icon unverified" title="Icon unverified">◇</span> Level <small class="formula-scope">(source)</small></a> × <wbr>0.004))) ≤ <wbr>1.7), <wbr>Branch((<a class="stat-reference" href="@wiki/stats/#stat--412912059"><span class="stat-icon-missing" role="img" aria-label="Icon unverified" title="Icon unverified">◇</span> Level <small class="formula-scope">(source)</small></a> &lt; <wbr>80), <wbr>1.4, <wbr>(1.08 + <wbr>(<a class="stat-reference" href="@wiki/stats/#stat--412912059"><span class="stat-icon-missing" role="img" aria-label="Icon unverified" title="Icon unverified">◇</span> Level <small class="formula-scope">(source)</small></a> × <wbr>0.004))), <wbr>1.7)) × <wbr>16.7 × <wbr><a class="stat-reference" href="@wiki/stats/#stat-1969273205"><span class="stat-icon-missing" role="img" aria-label="Icon unverified" title="Icon unverified">◇</span> XP divisor <small class="formula-scope">(source)</small></a>) − <wbr>12)</p><details class="formula-source"><summary>Original Unity formula</summary><pre><code>(((GetStat(source,-412912059)^Branch((Branch((GetStat(source,-412912059) &lt; 80),1.4,(1.08+(GetStat(source,-412912059)*0.004))) &lt;= 1.7),Branch((GetStat(source,-412912059) &lt; 80),1.4,(1.08+(GetStat(source,-412912059)*0.004))),1.7))*16.7*GetStat(source,1969273205))-12)</code></pre><p>Unity · <code>data.unity3d::sharedassets0.assets</code> · PathID 16387</p><p><code>maxValue / _formulaLinker / _formula · rid 126617797533631111</code></p></details></div>

` sharedassets0.assets PathID 22969 · _levelStat ` · ` ARPGEntity_Module_Level.GetCurrentLevel · RVA 0x87F7C0 `

Source Unity · ` data.unity3d::sharedassets0.assets ` · PathID 16480

## <img class="stat-icon" src="../public-assets/stats/394adb4d8c89269756e96865d48aeb6df2c6441ecafef74a1128dad49492c7c4.png" alt="" loading="lazy"> Life Steal Efficiency &#40;%&#41; { #stat--1459590084 }

ID · ` -1459590084 `

**Game description** · Regen \+0\.125 HP on normal kills and \+2\.5 HP on Elite kills\. Higher efficiency increases HP gained per kill\.

**Unit** · Percentage (serialized fraction)

Source Unity · ` Stat_Description_LifeSteal ` · ` data.unity3d::sharedassets0.assets ` · PathID 16481

## <img class="stat-icon" src="../public-assets/stats/b3b24a21013b8526c326481f082183e3d52ea265d14e46d7f0c73b2a5c91d867.png" alt="" loading="lazy"> Lightning Damage { #stat-217526346 }

ID · ` 217526346 `

**Game description** · Affects the amount of lightning damage dealt by your abilities\.

**Unit** · Display unit unconfirmed

Source Unity · ` Stat_Description_LightningDamage ` · ` data.unity3d::sharedassets0.assets ` · PathID 16484

## <img class="stat-icon" src="../public-assets/stats/b3b24a21013b8526c326481f082183e3d52ea265d14e46d7f0c73b2a5c91d867.png" alt="" loading="lazy"> Lightning Damage &#40;%&#41; { #stat--1439315223 }

ID · ` -1439315223 `

**Game description** · Affects the amount of lightning damage dealt by your abilities\.

**Unit** · Percentage (serialized fraction)

Source Unity · ` Stat_Description_LightningDamage ` · ` data.unity3d::sharedassets0.assets ` · PathID 16482

## <img class="stat-icon" src="../public-assets/stats/0913cd8af7b48e2af720fd9e2f5c0f50a75fa3c31ba26ce9993f40411f111239.png" alt="" loading="lazy"> Lightning Damage Multiplier { #stat-289068898 }

ID · ` 289068898 `

**Game description** · Multiply the amount of Lightning damage dealt\.

**Unit** · Display unit unconfirmed

Source Unity · ` Stat_Description_LightningPenetration ` · ` data.unity3d::sharedassets0.assets ` · PathID 16483

## <img class="stat-icon" src="../public-assets/stats/2f154db037264ffc504eac411a4bfbe99fa9344e6d8f12ba91aeb16d72529b4c.png" alt="" loading="lazy"> Lightning Resistance &#40;%&#41; { #stat-153888567 }

ID · ` 153888567 `

**Game description** · Determines your resistance to lightning damage, taking less damage in the process\.

**Unit** · Percentage (serialized fraction)

Source Unity · ` Stat_Description_LightningResistance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16486

## <img class="stat-icon" src="../public-assets/stats/9ae54565e58a291e21412929bb9bb4a3ddbaf62ea393e6c6690ba6a162039b46.png" alt="" loading="lazy"> Maximum Cold Resistance &#40;%&#41; { #stat-1562786720 }

ID · ` 1562786720 `

**Game description** · Determines your maximum cold resistance\.

**Unit** · Percentage (serialized fraction)

Source Unity · ` Stat_Description_MaximumColdResistance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16460

## <img class="stat-icon" src="../public-assets/stats/4c1ebc5c7e6a1039e8b0a5a7303824c47334a32941b2294b9e71b9d7eec0c97c.png" alt="" loading="lazy"> Maximum Fire Resistance &#40;%&#41; { #stat-122110380 }

ID · ` 122110380 `

**Game description** · Determines your maximum fire resistance\.

**Unit** · Percentage (serialized fraction)

Source Unity · ` Stat_Description_MaximumFireResistance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16470

## <img class="stat-icon" src="../public-assets/stats/72e5a6c8393faa7a4bc9b16c044bf89c173fb90df6c8f9856c38092ddd7fb6f6.png" alt="" loading="lazy"> Maximum Lightning Resistance &#40;%&#41; { #stat--1582074329 }

ID · ` -1582074329 `

**Game description** · Determines your maximum lightning resistance\.

**Unit** · Percentage (serialized fraction)

Source Unity · ` Stat_Description_MaximumLightningResistance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16485

## <img class="stat-icon" src="../public-assets/stats/1c88b0f5346520409c78e50bcef3fd3d9bcc93eed97130c64241a17045ca66c8.png" alt="" loading="lazy"> Maximum Physical Resistance &#40;%&#41; { #stat-1220215810 }

ID · ` 1220215810 `

**Game description** · Determines your maximum physical resistance\.

**Unit** · Percentage (serialized fraction)

Source Unity · ` Stat_Description_MaximumPhysicalResistance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16497

## <img class="stat-icon" src="../public-assets/stats/855423c4aa13c2b6b239a05a81cbf6e7d778b297dc166cf01f217da04fffff02.png" alt="" loading="lazy"> Movement Speed { #stat-411658539 }

ID · ` 411658539 `

**Game description** · Influences your movement speed\.

**Unit** · Display unit unconfirmed

**Verified configuration and formula** · Base speed used in the movement calculation for several enemies\. The calculation applies the movement\-speed modifier and accounts for slow resistance when that modifier is negative\.

**Scope of verification** · Movement units and the exact scope of the calculation for players remain unconfirmed\.

<div class="wiki-formula"><p class="formula-title">Serialized formula <small>· PathID 16580</small></p><p class="formula-expression">Branch((<a class="stat-reference" href="@wiki/stats/#stat--1427501575"><img class="stat-icon" src="../public-assets/stats/855423c4aa13c2b6b239a05a81cbf6e7d778b297dc166cf01f217da04fffff02.png" alt="" loading="lazy"> Movement Speed (%) <small class="formula-scope">(source)</small></a> ≥ <wbr>0), <wbr>(<a class="stat-reference" href="@wiki/stats/#stat-411658539"><img class="stat-icon" src="../public-assets/stats/855423c4aa13c2b6b239a05a81cbf6e7d778b297dc166cf01f217da04fffff02.png" alt="" loading="lazy"> Movement Speed <small class="formula-scope">(source)</small></a> × <wbr>(1 + <wbr><a class="stat-reference" href="@wiki/stats/#stat--1427501575"><img class="stat-icon" src="../public-assets/stats/855423c4aa13c2b6b239a05a81cbf6e7d778b297dc166cf01f217da04fffff02.png" alt="" loading="lazy"> Movement Speed (%) <small class="formula-scope">(source)</small></a>)), <wbr>((<a class="stat-reference" href="@wiki/stats/#stat-411658539"><img class="stat-icon" src="../public-assets/stats/855423c4aa13c2b6b239a05a81cbf6e7d778b297dc166cf01f217da04fffff02.png" alt="" loading="lazy"> Movement Speed <small class="formula-scope">(source)</small></a> × <wbr><a class="stat-reference" href="@wiki/stats/#stat--1844310897"><img class="stat-icon" src="../public-assets/stats/dbe1f970860c6d3afa9a0ff92fd3ed835e3cdefc63f35b307a706f1ff138aef0.png" alt="" loading="lazy"> Slow Resistance <small class="formula-scope">(source)</small></a>) + <wbr>(<a class="stat-reference" href="@wiki/stats/#stat-411658539"><img class="stat-icon" src="../public-assets/stats/855423c4aa13c2b6b239a05a81cbf6e7d778b297dc166cf01f217da04fffff02.png" alt="" loading="lazy"> Movement Speed <small class="formula-scope">(source)</small></a> × <wbr>(2 ^ <wbr><a class="stat-reference" href="@wiki/stats/#stat--1427501575"><img class="stat-icon" src="../public-assets/stats/855423c4aa13c2b6b239a05a81cbf6e7d778b297dc166cf01f217da04fffff02.png" alt="" loading="lazy"> Movement Speed (%) <small class="formula-scope">(source)</small></a>) × <wbr>(1 − <wbr><a class="stat-reference" href="@wiki/stats/#stat--1844310897"><img class="stat-icon" src="../public-assets/stats/dbe1f970860c6d3afa9a0ff92fd3ed835e3cdefc63f35b307a706f1ff138aef0.png" alt="" loading="lazy"> Slow Resistance <small class="formula-scope">(source)</small></a>))))</p><details class="formula-source"><summary>Original Unity formula</summary><pre><code>Branch((GetStat(source,-1427501575) &gt;= 0),(GetStat(source,411658539)*(1+GetStat(source,-1427501575))),((GetStat(source,411658539)*GetStat(source,-1844310897))+(GetStat(source,411658539)*(2^GetStat(source,-1427501575))*(1-GetStat(source,-1844310897)))))</code></pre><p>Unity · <code>data.unity3d::sharedassets0.assets</code> · PathID 16580</p><p><code>_data / _formula</code></p></details></div>

` sharedassets0.assets PathID 18700 · AIMovementData_Chase_Bat `

Source Unity · ` Stat_Description_MovementSpeed ` · ` data.unity3d::sharedassets0.assets ` · PathID 16490

## <img class="stat-icon" src="../public-assets/stats/855423c4aa13c2b6b239a05a81cbf6e7d778b297dc166cf01f217da04fffff02.png" alt="" loading="lazy"> Movement Speed &#40;%&#41; { #stat--1427501575 }

ID · ` -1427501575 `

**Game description** · Influences your movement speed\.

**Unit** · Percentage (serialized fraction)

Source Unity · ` Stat_Description_MovementSpeed ` · ` data.unity3d::sharedassets0.assets ` · PathID 16489

## <span class="stat-icon-missing" role="img" aria-label="Icon unverified" title="Icon unverified">◇</span> Overheal Capacity &#40;%&#41; { #stat-1910202602 }

ID · ` 1910202602 `

**Game description** · Maximum overheal as a percentage of maximum health\. Increasing capacity does not fill the reserve\.

**Unit** · Percentage (serialized fraction)

**Verified configuration and formula** · The capacity of the overheal reserve is maximum health multiplied by this fraction\.

**Scope of verification** · The game description states how a capacity change affects the current reserve\.

<div class="wiki-formula"><p class="formula-title">Serialized formula <small>· PathID 16582</small></p><p class="formula-expression">(<span class="formula-technical"><code>GetAttributeMax(source,-1822657751)</code></span> × <wbr><a class="stat-reference" href="@wiki/stats/#stat-1910202602"><span class="stat-icon-missing" role="img" aria-label="Icon unverified" title="Icon unverified">◇</span> Overheal Capacity (%) <small class="formula-scope">(source)</small></a>)</p><details class="formula-source"><summary>Original Unity formula</summary><pre><code>(GetAttributeMax(source,-1822657751)*GetStat(source,1910202602))</code></pre><p>Unity · <code>data.unity3d::sharedassets0.assets</code> · PathID 16582</p><p><code>_data / _formula</code></p></details></div>

` sharedassets0.assets PathID 16386 · maxValue `

Source Unity · ` Stat_Title_OverhealCapacity_Description ` · ` data.unity3d::sharedassets0.assets ` · PathID 16491

## <span class="stat-icon-missing" role="img" aria-label="Icon unverified" title="Icon unverified">◇</span> Overheal Decay Amount { #stat-1910202603 }

ID · ` 1910202603 `

**Game description** · Overheal lost at each decay tick\. Zero disables decay\.

**Unit** · Overheal HP per tick

**Verified code and formula** · Base overheal lost per tick\. The module applies the decay modifier before removing overheal\. An effective loss of zero disables decay\.

**Scope of verification** · Removal cannot exceed the remaining reserve\. The serialized base loss is 0\.5 HP\.

<div class="wiki-formula"><p class="formula-title">Serialized formula <small>· PathID 2896</small></p><p class="formula-expression">(<a class="stat-reference" href="@wiki/stats/#stat-1910202603"><span class="stat-icon-missing" role="img" aria-label="Icon unverified" title="Icon unverified">◇</span> Overheal Decay Amount <small class="formula-scope">(source)</small></a> × <wbr>(1 + <wbr><a class="stat-reference" href="@wiki/stats/#stat-1111063864"><span class="stat-icon-missing" role="img" aria-label="Icon unverified" title="Icon unverified">◇</span> Overheal decay amount (%) <small class="formula-scope">(source)</small></a>))</p><details class="formula-source"><summary>Original Unity formula</summary><pre><code>(GetStat(source,1910202603)*(1+GetStat(source,1111063864)))</code></pre><p>Unity · <code>data.unity3d::resources.assets</code> · PathID 2896</p><p><code>_decayAmount / _formulaLinker / _formula · rid 7608466127516598827</code></p></details></div>

` ARPGEntity_Module_Temp_OverhealDecay.Tick · RVA 0x888260 `

Source Unity · ` Stat_Title_OverhealDecayAmount_Description ` · ` data.unity3d::sharedassets0.assets ` · PathID 16492

## <span class="stat-icon-missing" role="img" aria-label="Icon unverified" title="Icon unverified">◇</span> Overheal decay amount &#40;%&#41; { #stat-1111063864 }

ID · ` 1111063864 `

**Unit** · Percentage (serialized fraction)

**Verified code and formula** · Modifies the amount of overheal lost per tick\. The base loss is multiplied by one plus this fraction\.

**Scope of verification** · The module ignores a negative or non\-finite loss and never removes more than the remaining reserve\.

<div class="wiki-formula"><p class="formula-title">Serialized formula <small>· PathID 2896</small></p><p class="formula-expression">(<a class="stat-reference" href="@wiki/stats/#stat-1910202603"><span class="stat-icon-missing" role="img" aria-label="Icon unverified" title="Icon unverified">◇</span> Overheal Decay Amount <small class="formula-scope">(source)</small></a> × <wbr>(1 + <wbr><a class="stat-reference" href="@wiki/stats/#stat-1111063864"><span class="stat-icon-missing" role="img" aria-label="Icon unverified" title="Icon unverified">◇</span> Overheal decay amount (%) <small class="formula-scope">(source)</small></a>))</p><details class="formula-source"><summary>Original Unity formula</summary><pre><code>(GetStat(source,1910202603)*(1+GetStat(source,1111063864)))</code></pre><p>Unity · <code>data.unity3d::resources.assets</code> · PathID 2896</p><p><code>_decayAmount / _formulaLinker / _formula · rid 7608466127516598827</code></p></details></div>

` ARPGEntity_Module_Temp_OverhealDecay.Tick · RVA 0x888260 `

Source Unity · ` data.unity3d::resources.assets ` · PathID 2789

## <span class="stat-icon-missing" role="img" aria-label="Icon unverified" title="Icon unverified">◇</span> Overheal Decay Interval { #stat-1910202604 }

ID · ` 1910202604 `

**Game description** · Seconds between overheal decay ticks\. Healing does not restart this timer\.

**Unit** · Seconds

**Verified code and formula** · Time between overheal ticks\. The module only applies decay with a finite, strictly positive interval\.

**Scope of verification** · The serialized base interval is approximately 0\.2 seconds\. How healing affects the timer is stated in the game description\.

<div class="wiki-formula"><p class="formula-title">Serialized formula <small>· PathID 2896</small></p><p class="formula-expression"><a class="stat-reference" href="@wiki/stats/#stat-1910202604"><span class="stat-icon-missing" role="img" aria-label="Icon unverified" title="Icon unverified">◇</span> Overheal Decay Interval <small class="formula-scope">(source)</small></a></p><details class="formula-source"><summary>Original Unity formula</summary><pre><code>GetStat(source,1910202604)</code></pre><p>Unity · <code>data.unity3d::resources.assets</code> · PathID 2896</p><p><code>_decayInterval / _formulaLinker / _formula · rid 7608466127516598829</code></p></details></div>

` ARPGEntity_Module_Temp_OverhealDecay.Tick · RVA 0x888260 `

Source Unity · ` Stat_Title_OverhealDecayInterval_Description ` · ` data.unity3d::sharedassets0.assets ` · PathID 16493

## <img class="stat-icon" src="../public-assets/stats/1bd93df45ed7c71e0c9e9f89ceba4ec764d4a96afcaeb57efc59a131ade027cf.png" alt="" loading="lazy"> Physical Damage { #stat--1329040019 }

ID · ` -1329040019 `

**Game description** · Affects the amount of physical damage dealt by your abilities\.

**Unit** · Display unit unconfirmed

Source Unity · ` Stat_Description_PhysicalDamage ` · ` data.unity3d::sharedassets0.assets ` · PathID 16496

## <img class="stat-icon" src="../public-assets/stats/1bd93df45ed7c71e0c9e9f89ceba4ec764d4a96afcaeb57efc59a131ade027cf.png" alt="" loading="lazy"> Physical Damage &#40;%&#41; { #stat-375307812 }

ID · ` 375307812 `

**Game description** · Affects the amount of physical damage dealt by your abilities\.

**Unit** · Percentage (serialized fraction)

Source Unity · ` Stat_Description_PhysicalDamage ` · ` data.unity3d::sharedassets0.assets ` · PathID 16494

## <img class="stat-icon" src="../public-assets/stats/49dbfb3210993e59d01e58fc82f602b2f8c9185a631bd03f6b9c8d9ef67540bf.png" alt="" loading="lazy"> Physical Damage Multiplier { #stat-1240293936 }

ID · ` 1240293936 `

**Game description** · Multiply the amount of Physical damage dealt\.

**Unit** · Display unit unconfirmed

Source Unity · ` Stat_Description_PhysicalPenetration ` · ` data.unity3d::sharedassets0.assets ` · PathID 16495

## <img class="stat-icon" src="../public-assets/stats/a7c44f74fd336c64853e8177389480e0374244f22f7994f4982bf396d5cc7b24.png" alt="" loading="lazy"> Physical Resistance &#40;%&#41; { #stat-2137905250 }

ID · ` 2137905250 `

**Game description** · Determines your resistance to physical damage, taking less damage in the process\.

**Unit** · Percentage (serialized fraction)

Source Unity · ` Stat_Description_PhysicalResistance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16498

## <img class="stat-icon" src="../public-assets/stats/d8399cf543dad2ac547e79901fa86e52c996e818a9a5b93a42252d5f00d7c123.png" alt="" loading="lazy"> Pickup Range { #stat--1969582225 }

ID · ` -1969582225 `

**Game description** · Determines the range at which you can collect items or orbs\.

**Unit** · Display unit unconfirmed

Source Unity · ` Stat_Description_PickupRange ` · ` data.unity3d::sharedassets0.assets ` · PathID 16500

## <img class="stat-icon" src="../public-assets/stats/d8399cf543dad2ac547e79901fa86e52c996e818a9a5b93a42252d5f00d7c123.png" alt="" loading="lazy"> Pickup Range &#40;%&#41; { #stat--1920634750 }

ID · ` -1920634750 `

**Game description** · Determines the range at which you can collect items or orbs\.

**Unit** · Percentage (serialized fraction)

Source Unity · ` Stat_Description_PickupRange ` · ` data.unity3d::sharedassets0.assets ` · PathID 16499

## <img class="stat-icon" src="../public-assets/stats/a9921fbc069c2af458c7ea27422672504aed1ac0014c70701298472598686183.png" alt="" loading="lazy"> Pierce Count { #stat-530049776 }

ID · ` 530049776 `

**Game description** · Determines how many times an ability can pierce through enemies, striking and applying effects to additional foes without being destroyed\.

**Unit** · Display unit unconfirmed

Source Unity · ` Stat_Description_PierceCount ` · ` data.unity3d::sharedassets0.assets ` · PathID 16508

## <img class="stat-icon" src="../public-assets/stats/226c10fc139c5e977f60d4160ecf83440f7d171ccc7146348009dc952ddb9567.png" alt="" loading="lazy"> Poison Chance { #stat-1687477670 }

ID · ` 1687477670 `

**Game description** · Increases the chance to inflict Poison on hitting an enemy, dealing damage over time\.

**Unit** · Percentage (serialized fraction)

Source Unity · ` Stat_Description_PoisonChance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16502

## <img class="stat-icon" src="../public-assets/stats/226c10fc139c5e977f60d4160ecf83440f7d171ccc7146348009dc952ddb9567.png" alt="" loading="lazy"> Poison Chance &#40;%&#41; { #stat-1955502493 }

ID · ` 1955502493 `

**Game description** · Increases the chance to inflict Poison on hitting an enemy, dealing damage over time\.

**Unit** · Percentage (serialized fraction)

Source Unity · ` Stat_Description_PoisonChance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16501

## <img class="stat-icon" src="../public-assets/stats/453b4c1ccc9d36079814657db8ecfeba99e2a3c62c4995365fc53df7e8de513d.png" alt="" loading="lazy"> Poison Power { #stat-62229812 }

ID · ` 62229812 `

**Game description** · The effect of Poison is more effective\. Dealing even more damage\.

**Unit** · Display unit unconfirmed

Source Unity · ` Stat_Description_PoisonPower ` · ` data.unity3d::sharedassets0.assets ` · PathID 16503

## <img class="stat-icon" src="../public-assets/stats/f9006a324fb3346835414732ee6bd8c0d351663697c132abe4d4b0b3fae7f0eb.png" alt="" loading="lazy"> Poison Stack { #stat-1748677144 }

ID · ` 1748677144 `

**Game description** · Determines the maximum number of Poison stacks that can be inflicted\.

**Unit** · Display unit unconfirmed

Source Unity · ` Stat_Description_PoisonStack ` · ` data.unity3d::sharedassets0.assets ` · PathID 16504

## <img class="stat-icon" src="../public-assets/stats/b84826196b02bd72c949e89271fc22078cac98935e47069884cf1830203aafca.png" alt="" loading="lazy"> Projectile Count { #stat--530233839 }

ID · ` -530233839 `

**Game description** · Number of additional projectiles added to your abilities\.

**Unit** · Count

<div class="wiki-formula"><p class="formula-title">Projectile count <small>· PathID 16596</small></p><p class="formula-expression"><a class="stat-reference" href="@wiki/stats/#stat--530233839"><img class="stat-icon" src="../public-assets/stats/b84826196b02bd72c949e89271fc22078cac98935e47069884cf1830203aafca.png" alt="" loading="lazy"> Projectile Count <small class="formula-scope">(source)</small></a></p><details class="formula-source"><summary>Original Unity formula</summary><pre><code>GetStat(source,-530233839)</code></pre><p>Unity · <code>data.unity3d::sharedassets0.assets</code> · PathID 16596</p><p><code>_data / _formula · offset 68</code></p></details></div>

Source Unity · ` Stat_Description_ProjectileCount ` · ` data.unity3d::sharedassets0.assets ` · PathID 16507

## <img class="stat-icon" src="../public-assets/stats/9b2665345ce216ed4466bffc743727b3dc39e750b20c8f611c3b11eaf1865dc1.png" alt="" loading="lazy"> Projectile Speed { #stat-631551606 }

ID · ` 631551606 `

**Game description** · Alter the speed of your projectiles\.

**Unit** · Display unit unconfirmed

<div class="wiki-formula"><p class="formula-title">Projectile speed <small>· PathID 16598</small></p><p class="formula-expression">(<a class="stat-reference" href="@wiki/stats/#stat-631551606"><img class="stat-icon" src="../public-assets/stats/9b2665345ce216ed4466bffc743727b3dc39e750b20c8f611c3b11eaf1865dc1.png" alt="" loading="lazy"> Projectile Speed <small class="formula-scope">(source)</small></a> × <wbr>(1 + <wbr><a class="stat-reference" href="@wiki/stats/#stat-1250534698"><img class="stat-icon" src="../public-assets/stats/9b2665345ce216ed4466bffc743727b3dc39e750b20c8f611c3b11eaf1865dc1.png" alt="" loading="lazy"> Projectile Speed (%) <small class="formula-scope">(source)</small></a>))</p><details class="formula-source"><summary>Original Unity formula</summary><pre><code>(GetStat(source,631551606)*(1+GetStat(source,1250534698)))</code></pre><p>Unity · <code>data.unity3d::sharedassets0.assets</code> · PathID 16598</p><p><code>_data / _formula · offset 68</code></p></details></div>

Source Unity · ` Stat_Description_ProjectileSpeed ` · ` data.unity3d::sharedassets0.assets ` · PathID 16510

## <img class="stat-icon" src="../public-assets/stats/9b2665345ce216ed4466bffc743727b3dc39e750b20c8f611c3b11eaf1865dc1.png" alt="" loading="lazy"> Projectile Speed &#40;%&#41; { #stat-1250534698 }

ID · ` 1250534698 `

**Game description** · Alter the speed of your projectiles\.

**Unit** · Percentage (serialized fraction)

<div class="wiki-formula"><p class="formula-title">Projectile speed <small>· PathID 16598</small></p><p class="formula-expression">(<a class="stat-reference" href="@wiki/stats/#stat-631551606"><img class="stat-icon" src="../public-assets/stats/9b2665345ce216ed4466bffc743727b3dc39e750b20c8f611c3b11eaf1865dc1.png" alt="" loading="lazy"> Projectile Speed <small class="formula-scope">(source)</small></a> × <wbr>(1 + <wbr><a class="stat-reference" href="@wiki/stats/#stat-1250534698"><img class="stat-icon" src="../public-assets/stats/9b2665345ce216ed4466bffc743727b3dc39e750b20c8f611c3b11eaf1865dc1.png" alt="" loading="lazy"> Projectile Speed (%) <small class="formula-scope">(source)</small></a>))</p><details class="formula-source"><summary>Original Unity formula</summary><pre><code>(GetStat(source,631551606)*(1+GetStat(source,1250534698)))</code></pre><p>Unity · <code>data.unity3d::sharedassets0.assets</code> · PathID 16598</p><p><code>_data / _formula · offset 68</code></p></details></div>

Source Unity · ` Stat_Description_ProjectileSpeed ` · ` data.unity3d::sharedassets0.assets ` · PathID 16509

## <span class="stat-icon-missing" role="img" aria-label="Icon unverified" title="Icon unverified">◇</span> Room Reward Multiplier { #stat--1031067952 }

ID · ` -1031067952 `

**Unit** · Display unit unconfirmed

Exact behaviour remains unconfirmed.

Source Unity · ` data.unity3d::resources.assets ` · PathID 2790

## <span class="stat-icon-missing" role="img" aria-label="Icon unverified" title="Icon unverified">◇</span> Shield strength { #stat-1712048563 }

ID · ` 1712048563 `

**Unit** · Display unit unconfirmed

Exact behaviour remains unconfirmed.

Source Unity · ` data.unity3d::resources.assets ` · PathID 2791

## <img class="stat-icon" src="../public-assets/stats/6c8b3562affd49461eca1ba701afb08874382cae8617808fc932f067a57c3bc1.png" alt="" loading="lazy"> Shock Chance { #stat--201340349 }

ID · ` -201340349 `

**Game description** · Increases the chance to inflict Shock on hitting an enemy, multiplying the damage taken by 50% and dealing damage\.

**Unit** · Percentage (serialized fraction)

Source Unity · ` Stat_Description_ShockChance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16513

## <img class="stat-icon" src="../public-assets/stats/6c8b3562affd49461eca1ba701afb08874382cae8617808fc932f067a57c3bc1.png" alt="" loading="lazy"> Shock Chance &#40;%&#41; { #stat-883058374 }

ID · ` 883058374 `

**Game description** · Increases the chance to inflict Shock on hitting an enemy, multiplying the damage taken by 50% and dealing damage\.

**Unit** · Percentage (serialized fraction)

Source Unity · ` Stat_Description_ShockChance ` · ` data.unity3d::sharedassets0.assets ` · PathID 16512

## <img class="stat-icon" src="../public-assets/stats/6c5c4151344f56aa64b965b888c1079b3382c2c3a9595f0a057122ae5f5943e2.png" alt="" loading="lazy"> Shock Power { #stat-2069118412 }

ID · ` 2069118412 `

**Game description** · The effect of Shock is more effective\. Multiplies damage further\.

**Unit** · Display unit unconfirmed

Source Unity · ` Stat_Description_ShockPower ` · ` data.unity3d::sharedassets0.assets ` · PathID 16511

## <img class="stat-icon" src="../public-assets/stats/900c8f3ed8c40ffb1a072a6670469edb4401dd457273b5824d0c9f75f7df904d.png" alt="" loading="lazy"> Shock Stack { #stat-1056975688 }

ID · ` 1056975688 `

**Game description** · Determines the maximum number of Shock stacks that can be inflicted\.

**Unit** · Display unit unconfirmed

Source Unity · ` Stat_Description_ShockStack ` · ` data.unity3d::sharedassets0.assets ` · PathID 16514

## <img class="stat-icon" src="../public-assets/stats/dbe1f970860c6d3afa9a0ff92fd3ed835e3cdefc63f35b307a706f1ff138aef0.png" alt="" loading="lazy"> Slow Resistance { #stat--1844310897 }

ID · ` -1844310897 `

**Game description** · Tenacity reduces the impact of slows and various control effects

**Unit** · Display unit unconfirmed

Source Unity · ` Stat_Description_Tenacity ` · ` data.unity3d::sharedassets0.assets ` · PathID 16517

## <img class="stat-icon" src="../public-assets/stats/8634a9b53a54481dc9558adcaad82ad1914921856f7f0cd910951d750c32e608.png" alt="" loading="lazy"> Stamina cooldown { #stat-830812871 }

ID · ` 830812871 `

**Unit** · Display unit unconfirmed

**Verified configuration and formula** · Base delay used to recover a charge in the verified evade setups, including Flame Dash\.

**Scope of verification** · The display unit and other recharge conditions remain unconfirmed\.

<div class="wiki-formula"><p class="formula-title">Serialized formula <small>· PathID 16600</small></p><p class="formula-expression">(<a class="stat-reference" href="@wiki/stats/#stat-830812871"><img class="stat-icon" src="../public-assets/stats/8634a9b53a54481dc9558adcaad82ad1914921856f7f0cd910951d750c32e608.png" alt="" loading="lazy"> Stamina cooldown <small class="formula-scope">(source)</small></a> × <wbr>(1 / <wbr>(1 + <wbr><a class="stat-reference" href="@wiki/stats/#stat--485591111"><img class="stat-icon" src="../public-assets/stats/8634a9b53a54481dc9558adcaad82ad1914921856f7f0cd910951d750c32e608.png" alt="" loading="lazy"> Stamina recovery rate (%) <small class="formula-scope">(source)</small></a>)))</p><details class="formula-source"><summary>Original Unity formula</summary><pre><code>(GetStat(source,830812871)*(1/(1+GetStat(source,-485591111))))</code></pre><p>Unity · <code>data.unity3d::sharedassets0.assets</code> · PathID 16600</p><p><code>_data / _formula</code></p></details></div>

` sharedassets0.assets PathID 16376 · _stackCooldownFormula `

Source Unity · ` data.unity3d::sharedassets0.assets ` · PathID 16515

## <img class="stat-icon" src="../public-assets/stats/8634a9b53a54481dc9558adcaad82ad1914921856f7f0cd910951d750c32e608.png" alt="" loading="lazy"> Stamina point max { #stat--412042601 }

ID · ` -412042601 `

**Unit** · Charges

**Verified configuration and formula** · Sets the maximum charge count in the verified evade setups, including Flame Dash\.

**Scope of verification** · The final conversion to an integer and other consumers remain unconfirmed\.

<div class="wiki-formula"><p class="formula-title">Serialized formula <small>· PathID 16599</small></p><p class="formula-expression"><a class="stat-reference" href="@wiki/stats/#stat--412042601"><img class="stat-icon" src="../public-assets/stats/8634a9b53a54481dc9558adcaad82ad1914921856f7f0cd910951d750c32e608.png" alt="" loading="lazy"> Stamina point max <small class="formula-scope">(source)</small></a></p><details class="formula-source"><summary>Original Unity formula</summary><pre><code>GetStat(source,-412042601)</code></pre><p>Unity · <code>data.unity3d::sharedassets0.assets</code> · PathID 16599</p><p><code>_data / _formula</code></p></details></div>

` sharedassets0.assets PathID 16376 · _maxStackFormula `

Source Unity · ` data.unity3d::sharedassets0.assets ` · PathID 16516

## <img class="stat-icon" src="../public-assets/stats/8634a9b53a54481dc9558adcaad82ad1914921856f7f0cd910951d750c32e608.png" alt="" loading="lazy"> Stamina recovery rate &#40;%&#41; { #stat--485591111 }

ID · ` -485591111 `

**Unit** · Percentage (serialized fraction)

**Verified configuration and formula** · A positive rate reduces the charge recovery delay in the verified setups\. The base delay is divided by one plus the rate\.

**Scope of verification** · This formula applies to Flame Dash and other setups that reference it\.

<div class="wiki-formula"><p class="formula-title">Serialized formula <small>· PathID 16600</small></p><p class="formula-expression">(<a class="stat-reference" href="@wiki/stats/#stat-830812871"><img class="stat-icon" src="../public-assets/stats/8634a9b53a54481dc9558adcaad82ad1914921856f7f0cd910951d750c32e608.png" alt="" loading="lazy"> Stamina cooldown <small class="formula-scope">(source)</small></a> × <wbr>(1 / <wbr>(1 + <wbr><a class="stat-reference" href="@wiki/stats/#stat--485591111"><img class="stat-icon" src="../public-assets/stats/8634a9b53a54481dc9558adcaad82ad1914921856f7f0cd910951d750c32e608.png" alt="" loading="lazy"> Stamina recovery rate (%) <small class="formula-scope">(source)</small></a>)))</p><details class="formula-source"><summary>Original Unity formula</summary><pre><code>(GetStat(source,830812871)*(1/(1+GetStat(source,-485591111))))</code></pre><p>Unity · <code>data.unity3d::sharedassets0.assets</code> · PathID 16600</p><p><code>_data / _formula</code></p></details></div>

` sharedassets0.assets PathID 16376 · _stackCooldownFormula `

Source Unity · ` data.unity3d::resources.assets ` · PathID 2792

## <img class="stat-icon" src="../public-assets/stats/226e54ad60c0d21105ca530196b45c4362ff0f78e3e04530a0b5de33d602305c.png" alt="" loading="lazy"> Thorn { #stat--1417792752 }

ID · ` -1417792752 `

**Unit** · Display unit unconfirmed

Exact behaviour remains unconfirmed.

Source Unity · ` data.unity3d::resources.assets ` · PathID 2793

## <span class="stat-icon-missing" role="img" aria-label="Icon unverified" title="Icon unverified">◇</span> XP divisor { #stat-1969273205 }

ID · ` 1969273205 `

**Unit** · Dimensionless multiplier

**Verified configuration and formula** · This factor multiplies the level\-dependent part of the experience maximum\. The constant 12 is subtracted after multiplication\.

**Scope of verification** · This is the formula for the level module’s XP attribute\. How this factor is assigned during a run remains unconfirmed\.

<div class="wiki-formula"><p class="formula-title">Serialized formula <small>· PathID 16387</small></p><p class="formula-expression">(((<a class="stat-reference" href="@wiki/stats/#stat--412912059"><span class="stat-icon-missing" role="img" aria-label="Icon unverified" title="Icon unverified">◇</span> Level <small class="formula-scope">(source)</small></a> ^ <wbr>Branch((Branch((<a class="stat-reference" href="@wiki/stats/#stat--412912059"><span class="stat-icon-missing" role="img" aria-label="Icon unverified" title="Icon unverified">◇</span> Level <small class="formula-scope">(source)</small></a> &lt; <wbr>80), <wbr>1.4, <wbr>(1.08 + <wbr>(<a class="stat-reference" href="@wiki/stats/#stat--412912059"><span class="stat-icon-missing" role="img" aria-label="Icon unverified" title="Icon unverified">◇</span> Level <small class="formula-scope">(source)</small></a> × <wbr>0.004))) ≤ <wbr>1.7), <wbr>Branch((<a class="stat-reference" href="@wiki/stats/#stat--412912059"><span class="stat-icon-missing" role="img" aria-label="Icon unverified" title="Icon unverified">◇</span> Level <small class="formula-scope">(source)</small></a> &lt; <wbr>80), <wbr>1.4, <wbr>(1.08 + <wbr>(<a class="stat-reference" href="@wiki/stats/#stat--412912059"><span class="stat-icon-missing" role="img" aria-label="Icon unverified" title="Icon unverified">◇</span> Level <small class="formula-scope">(source)</small></a> × <wbr>0.004))), <wbr>1.7)) × <wbr>16.7 × <wbr><a class="stat-reference" href="@wiki/stats/#stat-1969273205"><span class="stat-icon-missing" role="img" aria-label="Icon unverified" title="Icon unverified">◇</span> XP divisor <small class="formula-scope">(source)</small></a>) − <wbr>12)</p><details class="formula-source"><summary>Original Unity formula</summary><pre><code>(((GetStat(source,-412912059)^Branch((Branch((GetStat(source,-412912059) &lt; 80),1.4,(1.08+(GetStat(source,-412912059)*0.004))) &lt;= 1.7),Branch((GetStat(source,-412912059) &lt; 80),1.4,(1.08+(GetStat(source,-412912059)*0.004))),1.7))*16.7*GetStat(source,1969273205))-12)</code></pre><p>Unity · <code>data.unity3d::sharedassets0.assets</code> · PathID 16387</p><p><code>maxValue / _formulaLinker / _formula · rid 126617797533631111</code></p></details></div>

` sharedassets0.assets PathID 22969 · _xpAttribute ` · ` sharedassets0.assets PathID 16387 · maxValue `

Source Unity · ` data.unity3d::sharedassets0.assets ` · PathID 16518
