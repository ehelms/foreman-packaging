#!/usr/bin/env ruby

Dir.mkdir('tmp_repo') unless File.exist?('tmp_repo')

spec_dirs = if ARGV[0]
              if ARGV[0].include?('/')
                Dir.glob("#{ARGV[0]}*.spec")
              else
                Dir.glob("#{ARGV[0]}*/*.spec")
              end
            else
              Dir.glob('**/*.spec')
            end

spec_dirs.each do |dir|
  package = File.basename(dir).gsub('.spec', '')
  if (srpm = Dir.glob("tmp_repo/#{package}*").first)
    File.delete(srpm)
  end

  Dir.chdir(File.dirname(dir)) do
    system('../setup_sources.sh .')
    system('tito build --test --srpm --dist=.el7 --output ../tmp_repo')
  end
end

spec_dirs.each do |dir|
  spec = File.basename(dir)
  package = spec.gsub('.spec', '')

  #next if Dir.glob("build_repo/results/**/#{package}*.el7/*.rpm").first
  puts "Building for #{package}"
  system("mockchain -r mock/el7-scl.cfg --recurse -l build_repo tmp_repo/#{package}*")
end
