<template>
  <div class="home">
    <!-- Hero Section -->
    <section class="gradient-bg text-white py-20 md:py-32">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
          <div class="fade-in-up">
            <h1 class="text-4xl md:text-6xl font-bold mb-6 font-bengali leading-tight">
              স্বাগতম 🌾
              <br />
              <span class="text-green-200">মায়োমি নিশাত এগ্রো ফার্মে</span>
            </h1>
            <p class="text-xl md:text-2xl mb-8 text-green-100 font-bengali leading-relaxed">
              প্রকৃতির ছোঁয়ায়, মানসম্মত কৃষি উৎপাদনে একটি বিশ্বাসযোগ্য নাম
            </p>
            <div class="flex flex-wrap gap-4">
              <router-link to="/products" class="bg-white text-primary-600 px-8 py-4 rounded-lg font-semibold hover:bg-gray-100 transition-all duration-300 shadow-xl hover:shadow-2xl font-bengali">
                পণ্য দেখুন
              </router-link>
              <router-link to="/contact" class="bg-primary-800 text-white px-8 py-4 rounded-lg font-semibold hover:bg-primary-900 transition-all duration-300 shadow-xl hover:shadow-2xl font-bengali">
                যোগাযোগ করুন
              </router-link>
            </div>
          </div>
          <div class="hidden md:block float-animation">
            <img 
              src="https://images.unsplash.com/photo-1625246333195-78d9c38ad449?w=600" 
              alt="Farm" 
              class="rounded-2xl shadow-2xl"
            />
          </div>
        </div>
      </div>
    </section>

    <!-- Features Section -->
    <section class="py-20 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="section-title">🎯 আমাদের বৈশিষ্ট্য</h2>
          <p class="text-gray-600 text-lg font-bengali">কেন আমাদের বেছে নিবেন?</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          <div class="card p-6 text-center hover:scale-105 transition-transform duration-300">
            <div class="text-5xl mb-4">🌱</div>
            <h3 class="text-xl font-bold mb-3 font-bengali">১০০% প্রাকৃতিক</h3>
            <p class="text-gray-600 font-bengali">কোনো রাসায়নিক ছাড়াই প্রাকৃতিকভাবে উৎপাদিত</p>
          </div>

          <div class="card p-6 text-center hover:scale-105 transition-transform duration-300">
            <div class="text-5xl mb-4">✅</div>
            <h3 class="text-xl font-bold mb-3 font-bengali">মানসম্মত পণ্য</h3>
            <p class="text-gray-600 font-bengali">সর্বোচ্চ মানের পণ্য নিশ্চিত করা হয়</p>
          </div>

          <div class="card p-6 text-center hover:scale-105 transition-transform duration-300">
            <div class="text-5xl mb-4">🚚</div>
            <h3 class="text-xl font-bold mb-3 font-bengali">তাজা সরবরাহ</h3>
            <p class="text-gray-600 font-bengali">খামার থেকে সরাসরি আপনার কাছে</p>
          </div>

          <div class="card p-6 text-center hover:scale-105 transition-transform duration-300">
            <div class="text-5xl mb-4">💰</div>
            <h3 class="text-xl font-bold mb-3 font-bengali">সাশ্রয়ী মূল্য</h3>
            <p class="text-gray-600 font-bengali">ন্যায্য ও প্রতিযোগিতামূলক দামে</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Products Preview Section -->
    <section class="py-20 bg-gray-50">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="section-title">🛒 আমাদের পণ্যসমূহ</h2>
          <p class="text-gray-600 text-lg font-bengali">আমরা যা উৎপাদন করি</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <!-- Fish -->
          <div class="card group cursor-pointer">
            <div class="relative overflow-hidden h-64">
              <img 
                src="https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=500" 
                alt="Fish" 
                class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
              />
              <div class="absolute inset-0 bg-gradient-to-t from-black/70 to-transparent flex items-end">
                <div class="p-6 text-white w-full">
                  <h3 class="text-2xl font-bold mb-2 font-bengali">🐟 মাছ চাষ</h3>
                  <p class="text-gray-200 font-bengali">পাঙ্গাশ, শিং, তেলাপিয়া, রুই</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Dairy -->
          <div class="card group cursor-pointer">
            <div class="relative overflow-hidden h-64">
              <img 
                src="https://images.unsplash.com/photo-1628088062854-d1870b4553da?w=500" 
                alt="Dairy" 
                class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
              />
              <div class="absolute inset-0 bg-gradient-to-t from-black/70 to-transparent flex items-end">
                <div class="p-6 text-white w-full">
                  <h3 class="text-2xl font-bold mb-2 font-bengali">🐄 দুধ উৎপাদন</h3>
                  <p class="text-gray-200 font-bengali">১০০% বিশুদ্ধ গরুর দুধ</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Poultry -->
          <div class="card group cursor-pointer">
            <div class="relative overflow-hidden h-64">
              <img 
                src="https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?w=500" 
                alt="Poultry" 
                class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
              />
              <div class="absolute inset-0 bg-gradient-to-t from-black/70 to-transparent flex items-end">
                <div class="p-6 text-white w-full">
                  <h3 class="text-2xl font-bold mb-2 font-bengali">🐔 মুরগি পালন</h3>
                  <p class="text-gray-200 font-bengali">ব্রয়লার, দেশি ও লেয়ার</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Rice -->
          <div class="card group cursor-pointer">
            <div class="relative overflow-hidden h-64">
              <img 
                src="https://images.unsplash.com/photo-1586201375761-83865001e31c?w=500" 
                alt="Rice" 
                class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
              />
              <div class="absolute inset-0 bg-gradient-to-t from-black/70 to-transparent flex items-end">
                <div class="p-6 text-white w-full">
                  <h3 class="text-2xl font-bold mb-2 font-bengali">🌾 ধান ও বীজ</h3>
                  <p class="text-gray-200 font-bengali">উন্নতমানের বীজ উৎপাদন</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Eggs -->
          <div class="card group cursor-pointer">
            <div class="relative overflow-hidden h-64">
              <img 
                src="https://images.unsplash.com/photo-1582722872445-44dc5f7e3c8f?w=500" 
                alt="Eggs" 
                class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
              />
              <div class="absolute inset-0 bg-gradient-to-t from-black/70 to-transparent flex items-end">
                <div class="p-6 text-white w-full">
                  <h3 class="text-2xl font-bold mb-2 font-bengali">🥚 তাজা ডিম</h3>
                  <p class="text-gray-200 font-bengali">খামারের জৈব ডিম</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Mangoes -->
          <div class="card group cursor-pointer">
            <div class="relative overflow-hidden h-64">
              <img 
                src="https://images.unsplash.com/photo-1591073113125-e46713c829ed?w=500" 
                alt="Mangoes" 
                class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
              />
              <div class="absolute inset-0 bg-gradient-to-t from-black/70 to-transparent flex items-end">
                <div class="p-6 text-white w-full">
                  <h3 class="text-2xl font-bold mb-2 font-bengali">🥭 মৌসুমি আম</h3>
                  <p class="text-gray-200 font-bengali">প্রাকৃতিকভাবে পাকা আম</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="text-center mt-12">
          <router-link to="/products" class="btn-primary inline-block">
            সকল পণ্য দেখুন
          </router-link>
        </div>
      </div>
    </section>

    <!-- Goals Section -->
    <section class="py-20 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="section-title">🌿 আমাদের লক্ষ্য</h2>
          <p class="text-gray-600 text-lg font-bengali">আমরা কী করতে চাই</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div class="flex items-start space-x-4 p-6 bg-gray-50 rounded-xl hover:shadow-lg transition-shadow">
            <div class="text-3xl">👉</div>
            <div>
              <h3 class="text-xl font-bold mb-2 font-bengali">নিরাপদ খাদ্য উৎপাদন</h3>
              <p class="text-gray-600 font-bengali">প্রাকৃতিক ও স্বাস্থ্যকর খাদ্য উৎপাদন করা</p>
            </div>
          </div>

          <div class="flex items-start space-x-4 p-6 bg-gray-50 rounded-xl hover:shadow-lg transition-shadow">
            <div class="text-3xl">👉</div>
            <div>
              <h3 class="text-xl font-bold mb-2 font-bengali">আধুনিক প্রযুক্তি</h3>
              <p class="text-gray-600 font-bengali">আধুনিক কৃষি প্রযুক্তির ব্যবহার</p>
            </div>
          </div>

          <div class="flex items-start space-x-4 p-6 bg-gray-50 rounded-xl hover:shadow-lg transition-shadow">
            <div class="text-3xl">👉</div>
            <div>
              <h3 class="text-xl font-bold mb-2 font-bengali">কর্মসংস্থান সৃষ্টি</h3>
              <p class="text-gray-600 font-bengali">স্থানীয় কর্মসংস্থান সৃষ্টি ও কৃষকের উন্নয়ন</p>
            </div>
          </div>

          <div class="flex items-start space-x-4 p-6 bg-gray-50 rounded-xl hover:shadow-lg transition-shadow">
            <div class="text-3xl">👉</div>
            <div>
              <h3 class="text-xl font-bold mb-2 font-bengali">পরিবেশবান্ধব</h3>
              <p class="text-gray-600 font-bengali">পরিবেশবান্ধব কৃষি ব্যবস্থার প্রচার</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="gradient-bg text-white py-20">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="text-3xl md:text-5xl font-bold mb-6 font-bengali">
          আমাদের সাথে যুক্ত হন
        </h2>
        <p class="text-xl mb-8 text-green-100 font-bengali">
          মানসম্মত ও নিরাপদ কৃষিপণ্যের জন্য আজই যোগাযোগ করুন
        </p>
        <div class="flex flex-wrap justify-center gap-4">
          <a href="tel:+8801711727357" class="bg-white text-primary-600 px-8 py-4 rounded-lg font-semibold hover:bg-gray-100 transition-all duration-300 shadow-xl hover:shadow-2xl font-bengali">
            📞 +8801711727357
          </a>
          <a href="mailto:nishat@manishatagro.com" class="bg-primary-800 text-white px-8 py-4 rounded-lg font-semibold hover:bg-primary-900 transition-all duration-300 shadow-xl hover:shadow-2xl font-bengali">
            📧 ইমেইল করুন
          </a>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'Home'
}
</script>

<style scoped>
</style>
