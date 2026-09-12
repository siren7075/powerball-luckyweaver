# 🌟 Lucky Numbers Weighted Feature - Steering Document

## Overview
Add a **Personal Lucky Numbers Selection** feature that allows users to select their own "lucky numbers" and assign custom weights to them, influencing the generated number combinations.

**Feature Name (中文):** 幸运数字加权功能  
**Feature Name (EN):** Lucky Numbers Weighted Generator

---

## Feature Description

### User Experience
Users can:
1. **Select lucky numbers** - Choose any numbers from 1-69 (white balls) and 1-26 (red ball)
2. **Assign weights** - Set individual weights for each selected number (e.g., 0.5x to 2.0x)
3. **Toggle on/off** - Enable/disable lucky numbers weighting independently from decay weighting
4. **Save presets** - Optionally save favorite lucky number configurations
5. **Generate with bias** - Generate lottery numbers with increased probability of their lucky numbers

### Example Workflow
```
User: "I like numbers 7, 13, 21 (lucky in my culture)"
  → Select [7, 13, 21] with weights [1.5x, 1.5x, 1.5x]
  
User: "I also have a lucky red ball: 7"
  → Select red ball 7 with weight 2.0x

Click "Generate" 
  → System generates numbers with higher probability of including 7, 13, 21 (and red 7)
```

---

## Technical Implementation

### 1. Database/Storage Layer
```python
# User's lucky numbers configuration
lucky_config = {
    "enabled": True,
    "white_balls": {
        "7": 1.5,      # number: weight
        "13": 1.5,
        "21": 1.5,
    },
    "red_ball": {
        "7": 2.0       # optional red ball
    },
    "preset_name": "My Lucky Numbers",  # optional
    "created_at": timestamp
}
```

### 2. Backend Algorithm Changes
**File:** `powerball_generator.py`

```python
def generate_with_lucky_weights(
    white_balls=69,
    red_balls=26,
    select_count=5,
    weight_strength=0.6,      # decay weighting strength (0-1)
    periods=5,                 # for decay algorithm
    lucky_config=None,         # new parameter
    lucky_strength=1.0         # multiplier for lucky weights (0-2)
):
    """
    Generate Powerball numbers combining:
    1. Decay-based weighting (existing algorithm)
    2. Lucky numbers weighting (new feature)
    
    Algorithm:
    - Start with base decay probabilities
    - Apply lucky number multipliers
    - Normalize probabilities to sum = 1
    - Sample from weighted distribution
    """
    
    # Step 1: Calculate decay weights (existing)
    decay_weights = calculate_decay_weights(...)
    
    # Step 2: Apply lucky number weights (new)
    if lucky_config and lucky_config.get("enabled"):
        for number, weight in lucky_config["white_balls"].items():
            idx = int(number) - 1
            decay_weights[idx] *= (1 + (weight - 1) * lucky_strength)
    
    # Step 3: Normalize & sample
    probabilities = decay_weights / decay_weights.sum()
    selected = np.random.choice(
        range(1, white_balls + 1),
        size=select_count,
        replace=False,
        p=probabilities
    )
    
    return selected
```

### 3. API Changes
**Endpoint:** `POST /api/generate`

**New Request Parameters:**
```json
{
  "weight_strength": 0.6,
  "periods": 5,
  "count": 5,
  "lucky_numbers": {
    "enabled": true,
    "white_balls": {
      "7": 1.5,
      "13": 1.5,
      "21": 1.5
    },
    "red_ball": {
      "7": 2.0
    },
    "strength": 1.0
  }
}
```

**Response:** (unchanged structure, but influenced by lucky weights)
```json
{
  "numbers": [
    {"white": [7, 13, 21, 42, 55], "red": 7},
    ...
  ],
  "recent_numbers": [...],
  "analysis": {
    "lucky_numbers_used": [7, 13, 21],
    "lucky_red_used": 7,
    "probability_boost": 0.35
  }
}
```

---

## UI/UX Design

### Frontend Components

#### 1. Lucky Numbers Panel
```
┌─────────────────────────────────────┐
│ ✨ Lucky Numbers Configuration      │
├─────────────────────────────────────┤
│ □ Enable Lucky Numbers              │
│                                     │
│ White Balls (1-69):                │
│ [Input field: 7]  [Weight: 1.5x] ✕ │
│ [Input field: 13] [Weight: 1.5x] ✕ │
│ [Input field: 21] [Weight: 1.5x] ✕ │
│ [+ Add Number]                      │
│                                     │
│ Red Ball (1-26) [Optional]:        │
│ [Input field: 7]  [Weight: 2.0x] ✕ │
│                                     │
│ Strength: [====●====] 1.0x          │
│ (0.5x = subtle, 2.0x = strong)     │
│                                     │
│ [Save Preset] [Load Preset]         │
└─────────────────────────────────────┘
```

#### 2. Integration with Existing UI
- Place lucky numbers panel **above** the decay strength slider
- Collapse by default on mobile
- Add toggle icon next to each section for expand/collapse
- Show visual indicator when lucky numbers are active

#### 3. Results Display Enhancement
```
Generated Numbers:
[7] [13] [21] [42] [55] | [7] ✨

Analysis:
- Lucky Numbers Used: 7, 13, 21 (3/5 white, 1/1 red)
- Decay Contribution: 30%
- Lucky Numbers Contribution: 35%
- Random Selection: 35%
```

---

## Implementation Phases

### Phase 1: Backend (Week 1)
- [ ] Update `powerball_generator.py` with lucky weights algorithm
- [ ] Add `lucky_config` parameter to generation function
- [ ] Create unit tests for lucky weight calculations
- [ ] Update `/api/generate` endpoint to accept lucky_numbers parameter
- [ ] Validate lucky number inputs (range 1-69 for white, 1-26 for red)

### Phase 2: Frontend (Week 2)
- [ ] Build lucky numbers input panel in `templates/index.html`
- [ ] Add weight slider for each number
- [ ] Implement add/remove number buttons
- [ ] Add JavaScript validation for number ranges
- [ ] Wire up to API calls with lucky_config data

### Phase 3: Polish & Presets (Week 3)
- [ ] Add preset saving/loading (localStorage for now)
- [ ] Add visual feedback for lucky numbers in results
- [ ] Internationalize lucky numbers UI (Chinese & English)
- [ ] Mobile responsiveness optimization
- [ ] Documentation updates

### Phase 4: Testing & Deployment
- [ ] Integration tests combining decay + lucky weights
- [ ] User testing for UX flow
- [ ] Performance testing with edge cases
- [ ] Update FEATURES.md and README.md

---

## Configuration Details

### Weight Ranges
- **White ball weights:** 0.5x to 2.0x
  - 0.5x = slightly less likely
  - 1.0x = neutral (no effect)
  - 2.0x = significantly more likely
  
- **Red ball weights:** 0.5x to 2.5x (slightly higher range for red)

- **Strength multiplier:** 0-2.0x
  - Controls how much lucky weights influence results
  - 0 = lucky numbers ignored
  - 1.0 = full lucky weight effect
  - 2.0 = double lucky weight effect

### Validation Rules
```python
def validate_lucky_config(config):
    """
    - Max 20 white ball selections
    - Max 1 red ball selection
    - All numbers must be in valid range
    - Weights must be between 0.5 and 2.0
    - Config can be null (disabled)
    """
```

---

## Data & Analytics (Future)

### Track Usage
- How often lucky numbers feature is used
- Most popular lucky numbers
- Distribution of weight selections
- A/B test: decay vs lucky vs combined

### Optional: Store User Preferences (Future)
If we add user accounts:
```json
{
  "user_id": "...",
  "lucky_presets": [
    {"name": "Birthday Numbers", "config": {...}},
    {"name": "Cultural Lucky", "config": {...}}
  ]
}
```

---

## Internationalization (i18n)

### English Labels
- "Lucky Numbers Configuration"
- "Enable Lucky Numbers"
- "White Balls (1-69)"
- "Red Ball (1-26)"
- "Weight: "
- "Strength: "
- "Save Preset"

### Chinese Labels (中文)
- "幸运数字配置"
- "启用幸运数字"
- "白球 (1-69)"
- "红球 (1-26)"
- "权重:"
- "强度:"
- "保存预设"

---

## Risk Mitigation

### Edge Cases to Handle
1. **Empty selection** - Allow, just disable lucky numbers
2. **Duplicate numbers** - Prevent user from selecting same number twice
3. **Performance** - Ensure algorithm stays O(n) with normalization
4. **Mobile input** - Use number picker for better UX on mobile
5. **Browser storage** - Graceful fallback if localStorage unavailable

### Testing Strategy
```python
# Unit tests needed:
- test_lucky_weights_multiplication()
- test_weights_normalization()
- test_probability_distribution()
- test_combined_decay_and_lucky()
- test_edge_cases(empty, duplicate, out_of_range)
- test_performance_with_all_numbers_selected()
```

---

## Success Metrics

✅ **Feature Adoption**
- % of users enabling lucky numbers feature
- Average # of lucky numbers selected per user

✅ **Performance**
- Generation time remains < 100ms
- No noticeable UI lag

✅ **User Satisfaction**
- Feature is intuitive without documentation
- Positive feedback on UX

✅ **Code Quality**
- >90% test coverage for lucky weights logic
- No performance regressions

---

## Future Enhancements

1. **Smart Lucky Suggestions**
   - Based on cultural significance (日本, 中国, 西方 numbers)
   - Based on user input (birthday, anniversaries)
   - Popular numbers from community

2. **Weight Visualization**
   - Show probability curves for selected numbers
   - Compare decay-only vs lucky-only vs combined

3. **Advanced Combinations**
   - Lucky number pairs (e.g., "always include 7 and 13")
   - Constraints (e.g., "red must be from these")
   - Sequential patterns

4. **Machine Learning**
   - Learn user preferences over time
   - Recommend weights based on patterns

5. **Sharing**
   - Share lucky number presets with friends
   - Public preset library

---

## Definition of Done

- ✅ Backend algorithm implemented & tested
- ✅ API endpoint accepts & processes lucky_numbers parameter
- ✅ Frontend UI for lucky number selection complete
- ✅ Weight sliders functional
- ✅ Integration with decay weighting working correctly
- ✅ Results display shows contribution of lucky weights
- ✅ Internationalization complete
- ✅ Mobile responsive
- ✅ Documentation updated
- ✅ E2E tested on both English & Chinese UI
- ✅ No performance regressions

---

**Document Version:** 1.0  
**Last Updated:** 2026-09-12  
**Status:** Ready for implementation
