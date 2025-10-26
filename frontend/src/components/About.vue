<template>
  <div class="about">
    <!-- Hero Section -->
    <section class="gradient-bg text-white py-20">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h1 class="text-4xl md:text-5xl font-bold mb-6 font-bengali">আমাদের সম্পর্কে</h1>
        <p class="text-xl text-green-100 font-bengali max-w-3xl mx-auto">
          প্রকৃতির ছোঁয়ায়, মানসম্মত কৃষি উৎপাদনে একটি বিশ্বাসযোগ্য নাম
        </p>
      </div>
    </section>

    <!-- Main Content -->
    <section class="py-20 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center mb-20">
          <div>
            <h2 class="text-3xl md:text-4xl font-bold mb-6 font-bengali text-gray-800">
              মায়োমি নিশাত এগ্রো ফার্ম
            </h2>
            <p class="text-gray-600 mb-6 leading-relaxed font-bengali text-lg">
              <strong>মায়োমি নিশাত এগ্রো ফার্ম</strong> একটি আধুনিক ও বহুমুখী কৃষি প্রতিষ্ঠান, যেখানে প্রকৃতির সঙ্গে মিল রেখে টেকসই কৃষি উৎপাদন ও পশুপালনের সমন্বয় করা হয়েছে।
            </p>
            <p class="text-gray-600 mb-6 leading-relaxed font-bengali text-lg">
              আমাদের লক্ষ্য হলো দেশীয় খাদ্য উৎপাদনে আত্মনির্ভরতা গড়ে তোলা এবং গ্রাহকদের কাছে নিরাপদ ও মানসম্মত কৃষিপণ্য পৌঁছে দেওয়া।
            </p>
            <div class="flex gap-4">
              <router-link to="/products" class="btn-primary">
                পণ্য দেখুন
              </router-link>
              <router-link to="/contact" class="btn-secondary">
                যোগাযোগ করুন
              </router-link>
            </div>
          </div>
          <div>
            <img 
              src="https://images.unsplash.com/photo-1464226184884-fa280b87c399?w=600" 
              alt="Farm" 
              class="rounded-2xl shadow-2xl"
            />
          </div>
        </div>

        <!-- Farm Activities -->
        <div class="mb-20">
          <h2 class="text-3xl md:text-4xl font-bold mb-12 text-center font-bengali text-gray-800">
            আমাদের কার্যক্রম
          </h2>

          <div class="space-y-8">
            <!-- Fish Farming -->
            <div class="card p-8">
              <div class="flex items-start gap-6">
                <div class="text-5xl flex-shrink-0">🐟</div>
                <div>
                  <h3 class="text-2xl font-bold mb-4 font-bengali text-primary-700">মাছ চাষ</h3>
                  <p class="text-gray-600 mb-4 font-bengali leading-relaxed">
                    আমাদের ফার্মে রয়েছে অত্যাধুনিক পদ্ধতিতে পরিচালিত মাছের খামার। প্রতিটি পুকুরে স্বাস্থ্যকর পানির মান বজায় রাখা হয় এবং মাছের জন্য প্রাকৃতিক ও ভারসাম্যপূর্ণ খাদ্য সরবরাহ করা হয়।
                  </p>
                  <div class="flex flex-wrap gap-2">
                    <span class="px-4 py-2 bg-primary-100 text-primary-700 rounded-full text-sm font-bengali">পাঙ্গাশ</span>
                    <span class="px-4 py-2 bg-primary-100 text-primary-700 rounded-full text-sm font-bengali">শিং</span>
                    <span class="px-4 py-2 bg-primary-100 text-primary-700 rounded-full text-sm font-bengali">তেলাপিয়া</span>
                    <span class="px-4 py-2 bg-primary-100 text-primary-700 rounded-full text-sm font-bengali">রুই</span>
                    <span class="px-4 py-2 bg-primary-100 text-primary-700 rounded-full text-sm font-bengali">মৃগেল</span>
                  </div>
                </div>
              </div>
            </div>

            <!-- Cattle Farming -->
            <div class="card p-8">
              <div class="flex items-start gap-6">
                <div class="text-5xl flex-shrink-0">🐄</div>
                <div>
                  <h3 class="text-2xl font-bold mb-4 font-bengali text-primary-700">গরু পালন ও দুধ উৎপাদন</h3>
                  <p class="text-gray-600 mb-4 font-bengali leading-relaxed">
                    আমাদের ফার্মে দেশি ও বিদেশি জাতের গরু (ষাঁড় ও দুধেল গাভী) পালন করা হয়। উন্নত মানের খাদ্য, পরিচ্ছন্ন পরিবেশ ও নিয়মিত পশুচিকিৎসা সেবার মাধ্যমে আমরা উচ্চমানের দুধ উৎপাদন করে থাকি।
                  </p>
                  <div class="bg-green-50 border-l-4 border-primary-600 p-4 rounded">
                    <p class="text-gray-700 font-bengali font-semibold">
                      ✅ আমাদের গরুর দুধ ১০০% বিশুদ্ধ, কোনো প্রকার রাসায়নিক মিশ্রণ ছাড়া সংগ্রহ করা হয়।
                    </p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Poultry -->
            <div class="card p-8">
              <div class="flex items-start gap-6">
                <div class="text-5xl flex-shrink-0">🐔</div>
                <div>
                  <h3 class="text-2xl font-bold mb-4 font-bengali text-primary-700">মুরগি পালন</h3>
                  <p class="text-gray-600 mb-4 font-bengali leading-relaxed">
                    প্রতিটি খামারে স্বাস্থ্যবিধি মেনে মুরগি পালন করা হয় এবং আমরা নিরাপদ ও মানসম্মত মাংস ও ডিম উৎপাদনে প্রতিশ্রুতিবদ্ধ।
                  </p>
                  <ul class="space-y-2 text-gray-600 font-bengali">
                    <li class="flex items-center gap-2">
                      <span class="text-primary-600">•</span>
                      <span>ব্রয়লার মুরগি (মাংস উৎপাদনের জন্য)</span>
                    </li>
                    <li class="flex items-center gap-2">
                      <span class="text-primary-600">•</span>
                      <span>দেশি ও লেয়ার মুরগি (ডিম উৎপাদনের জন্য)</span>
                    </li>
                    <li class="flex items-center gap-2">
                      <span class="text-primary-600">•</span>
                      <span>কক মুরগি (প্রজননের জন্য)</span>
                    </li>
                  </ul>
                </div>
              </div>
            </div>

            <!-- Rice & Seeds -->
            <div class="card p-8">
              <div class="flex items-start gap-6">
                <div class="text-5xl flex-shrink-0">🌾</div>
                <div>
                  <h3 class="text-2xl font-bold mb-4 font-bengali text-primary-700">ধান ও বীজ উৎপাদন</h3>
                  <p class="text-gray-600 font-bengali leading-relaxed">
                    আমাদের ফার্মে উন্নতমানের ধান ও বীজ উৎপাদন করা হয়। আধুনিক কৃষি প্রযুক্তি ব্যবহারের মাধ্যমে আমরা অধিক ফলনশীল জাতের বীজ উৎপাদন করে থাকি, যা স্থানীয় কৃষকদের জন্য নির্ভরযোগ্য একটি উৎস।
                  </p>
                </div>
              </div>
            </div>

            <!-- Mangoes -->
            <div class="card p-8">
              <div class="flex items-start gap-6">
                <div class="text-5xl flex-shrink-0">🥭</div>
                <div>
                  <h3 class="text-2xl font-bold mb-4 font-bengali text-primary-700">মৌসুমি আম উৎপাদন</h3>
                  <p class="text-gray-600 font-bengali leading-relaxed">
                    প্রতিবছর মৌসুমে আমাদের বাগানে উৎপাদিত হয় সুস্বাদু ও প্রাকৃতিকভাবে চাষ করা আম। কোনো রাসায়নিক ছাড়াই আমরা আম পাকে এবং গ্রাহকদের কাছে পৌঁছে দিই তাজা ও বিশুদ্ধ ফল।
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Goals -->
        <div class="gradient-bg text-white rounded-3xl p-12">
          <h2 class="text-3xl md:text-4xl font-bold mb-8 text-center font-bengali">
            🌿 আমাদের লক্ষ্য
          </h2>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="flex items-start gap-4 bg-white/10 backdrop-blur-sm p-6 rounded-xl">
              <div class="text-3xl">👉</div>
              <p class="text-green-100 font-bengali text-lg">নিরাপদ, প্রাকৃতিক ও স্বাস্থ্যকর খাদ্য উৎপাদন</p>
            </div>
            <div class="flex items-start gap-4 bg-white/10 backdrop-blur-sm p-6 rounded-xl">
              <div class="text-3xl">👉</div>
              <p class="text-green-100 font-bengali text-lg">আধুনিক কৃষি প্রযুক্তির ব্যবহার</p>
            </div>
            <div class="flex items-start gap-4 bg-white/10 backdrop-blur-sm p-6 rounded-xl">
              <div class="text-3xl">👉</div>
              <p class="text-green-100 font-bengali text-lg">স্থানীয় কর্মসংস্থান সৃষ্টি ও কৃষকের উন্নয়ন</p>
            </div>
            <div class="flex items-start gap-4 bg-white/10 backdrop-blur-sm p-6 rounded-xl">
              <div class="text-3xl">👉</div>
              <p class="text-green-100 font-bengali text-lg">পরিবেশবান্ধব কৃষি ব্যবস্থার প্রচার</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'About'
}
</script>

<style scoped>
</style>
