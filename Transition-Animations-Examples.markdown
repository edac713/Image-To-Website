When it comes to product design, the importance of animation and motion can’t be overstated. As highlighted by the Nielsen Norman Group, they not only attract attention but enhance user enjoyment and help your product feel fresh and modern. When an animation is sophisticated enough, it can give users clear feedback on their actions, making the interface feel more intuitive.

Transition animations, in particular, are key in product design because they smoothly guide users from one stage to the next. They make products easier to use and more attractive, connecting different steps, and improving the overall product quality.

Because animation and motion play a vital role, product teams are aware of their importance. Designers will present these as prototypes to the broader team to demonstrate and test their product before launch. However, designing the perfect animation is an intricate endeavor. The challenge lies in finding the right balance between subtlety and emphasis. While there’s no shortage of online resources and articles delving into the intricacies of animations, a surprising number of products miss the mark on implementing them successfully.

This article focuses on transition animation specifically. The goal is to showcase the principles of transition animation with examples that are basic, compact, and can be used immediately by anyone in their design process. These insights are not rules set in stone, but rather guiding considerations for new product creation. Consider this your concise, practical guide to the art of transition animation.

# 6 principles for better transition animations

1. Fade in and out with opacity
2. Scale to add liveliness
3. Maintain consistent directionality
4. Balance speed
5. Prioritize, order, and group
6. Establish spatiality

```markdown

# 1. Fade in and out with opacity

Fade in / out

Fading in and out with opacity is a basic yet powerful principle. Utilizing this one technique alone can make a significant difference. When transitioning from the current screen to the next, you can deliver concise feedback by fading out irrelevant elements and letting the next part fade in. You can achieve this by turning the opacity value from 100 to 0 (or 0 to 100) in any design/prototyping tool.

## Figure 1–1
Toggle transition comparison. While the abrupt transition feels disconnected (see left image), adding the opacity effect feels smoother and more appealing (see right image).

## Figure 1–2
Menu opening comparison. Rather than abruptly cropping the menu from bottom to top as shown in the left image, utilizing a fade animation offers a gentler and more fluid transition, as depicted in the right image. This enhances user engagement with the menu.

## Figure 1–3
Here is a common example of using the fade animation to transition from one state to another. Additionally, it is animated using scale and vertical movement, which will be covered by the following principles.

As an advanced use case, this technique seamlessly integrates the interactions between two screen layers or sequences. By using this method, scene transitions become virtually undetectable to users. Many successful products employ this strategy for an enhanced user experience.

## Figure 1–4
The layer “Profile view” seamlessly moves while transitioning to the next state. A comprehensive breakdown can be found in the following image.

## Figure 1–5
This fluid transition was achieved by utilizing two “Profile view” layers — both small and large. By incorporating a scaling effect and smoothly fading between the two layers, the transition appears as though a singular title layer seamlessly bridges both screen states.

# 2. Scale to add liveliness

Scale with fade — a common usage of scale effect

Scaling introduces a dynamic, vibrant, and directional element to transitions. For example, when transitioning to the next screen, you can scale down the existing components and layers from 100% to 90%, along with fading out effects. For example, when displaying an overlay, you can scale down the current screen. This gives the impression of the overlay sliding from the higher layer, highlighting the connectivity between states. You can adjust the scaling value up and down, as desired. Scaling is typically used along with the first principle: fade in/out.

## Figure 2–1
Incorporating a scale effect with fading gives objects a more dynamic, livelier presence, as demonstrated in this example. This transition has a graceful motion, as if the layers are gliding in and out from top to bottom.

## Figure 2–2
Here are some examples of using the scale effect on text layers.

The left image shows how the active and inactive layers are highlighted using scale and a slight fade-out.

The right image also shows how to achieve a lively transition by scaling text and card layers.

## Figure 2–3
These two examples demonstrate how larger elements can be enhanced with scaling transitions.

(Left) A familiar instance of scaling can be seen in music apps during album cover transitions. As the music player overlay shrinks, the album cover smoothly scales down to a thumbnail size.

(Right) When opening an overlay, you can also scale down and show a slight peak of the previous screen to imply there’s a layer in the background. This is a default overlay style of iOS.

# 3. Maintain consistent directionality

Any movement, scaling, or motion in your product inherently suggests a direction. This indicates the context of your product and is a powerful way to make your transitions look consistent. It’s essential to document detailed directional information, such as when the element moves up or down, which side your overlay comes from, and more. Well designed products maintain clear and consistent directionality aligned with their context.

## Figure 3–1

(Left) It’s a typical social media app behavior to switch the viewing option with horizontal navigation. This way, you can swipe or tap the toggle to switch the view.

(Right) On the other hand, this app has a slightly different layout with vertical navigation. Swiping up and down is the way to switch the viewing option in this case.

## Figure 3–2
When it comes to scrolling through posts on each app example here, their directionality is opposed.

(Left) As expected, you can browse posts by swiping up and down.

(Right) Given that this app has a vertical navigation, scrolling through posts would be a horizontal action.

## Figure 3–3
Even when opening the menu or other relevant transitions, you can always imply the overall directionality of the app.

(Left) Opening the menu implies the vertical browsing experience of the app.

(Right) The menu elements appear from left to right, indicating the app’s horizontal browsing experience.

# 4. Balance speed

The right animation speed provides practical feedback and a meaningful experience. Transitions that are too slow can bore users, while overly fast transitions lack meaning. That’s why balancing speed is crucial. According to some articles, a speed from 100ms to 500ms is ideal and suitable for most cases. You can follow this as a guideline, but customize it to suit your product. That’s another way to create a distinctive product from others.

## Figure 4–1
Quick action, such as the toggle slider in this example, is important to have a proper speed to provide feedback to people. Since this is an in-page transition, it should be slightly faster than the page-to-page animation.

## Figure 4–2
For page-to-page transitions with many elements, there needs to be some context so people don’t feel disconnected from each state. This may be slightly slower than the in-page transition. However, that doesn’t necessarily mean slowing down your animation speed. Proper speed is still crucial to ensure that your product doesn’t feel slow.

# 5. Prioritize, order, and group

When transitioning multiple elements, rank them by importance to help users focus on key interactions. Instead of transitioning all at once, sequence them by priority. Group similar items together, then rank these groups. Irrelevant groups can be hidden entirely to maintain focus on crucial sections.

## Figure 5–1
If all the elements on this screen animated simultaneously, it would feel busy and complicated. This is why it has a cascading transition prioritized by importance. In this app, the primary elements should be the “Profile view” and the supporting chart since these elements exist in both states. Then secondary elements, which are less important than the primary ones, could follow next.

## Figure 5–2
It feels like music apps have complicated transitions when collapsing the player view. We can achieve a seamless transition by simply focusing on the cover and title layer. You can see a more detailed breakdown in the following image.

## Figure 5–3

(Left) This animation shows how the player overlay minimizes. As you can see, the existing music title and player element simply disappear by sliding down to the bottom.

(Right) After the screen minimizes, the new title layer appears. This way it doesn’t distract from the elements in the player and the cover scale animation.

# 6. Establish spatiality

Even though the user interaction area is limited to the device screen, designing the “invisible” space beyond the visible frame is crucial. Establishing spatiality helps users form a mental model of your product, enhancing their experience. Often, designers use multiple functional layers to introduce depth and spatiality to flat screens.

## Figure 6–1
This diagram shows a more detailed context of the music app. It depicts what functional layers in this app consist of and how the transition happens when the player view collapses and shows the overview screen with the minimized view.

## Figure 6–2
This example consists of two parts. First, it shows how the multiple layers of this social media app screen are made. Secondly, the comments overlay slides in from the bottom while the existing screen scales down and introduces the dark background layer — the lowest layer in the app.

In addition to that, all layers and elements with a directional movement are part of the spatiality. The following examples have the same interactions and layer elements, but use different spatial models to create a different feel for the product experience.

## Figure 6–3
As highlighted in the directionality principle, these two apps have different navigational structures. By looking beyond just the screen area and understanding the origin of transitions and movements, one can grasp the overarching spatial structure. Building such spatial frameworks significantly enriches the uniqueness of your product’s user experience.
```

As we’ve journeyed through the intricate world of transition animation, it’s evident how seemingly minute details can have a big impact on a user’s experience. The examples and principles presented here serve as a foundation, but you can draw your own inspiration from everyday interactions you have with existing apps and products. It’s through these personal experiences that you can learn to craft your own distinct animation style and provide unique experiences for users. Embrace these principles, experiment with what you encounter daily, and watch as your creations take on a life of their own.