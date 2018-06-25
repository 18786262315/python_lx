'''
unittest条件断言
tester: cc
此文仅做翻译只用，不介绍具体使用


'''
Skiptest()  # 在测试中引发此异常以跳过该异常。
_ShouldStop()  # 停止测试
_UnexpectedSuccess()  # 测试本来应该是失败的，但是没有失败
Skip()  # 无条件跳过测试。
skipIf(condition, reason)  # 条件为真时跳过测试
skipUnless(condition, reason)  # 条件为假时跳过测试
expectedFailure(test_item)  # 标记该测试预期就是失败，如果运行失败时，不算作失败用例。
_is_subtype(expected, basetype)  # 判断类型是否符合预期,暂时不知道干什么用的
addTypeEqualityFunc(typeobj, function) # 为自定义检查类提供检查方法
addCleanup( function , *args , **kwargs ) #添加针对每个测试用例执行完tearDown()方法之后的清理方法，添加进去的函数按照后进先出（LIFO）的顺序执行，当然，如果setUp()方法执行失败，那么不会执行tearDown()方法，自然也不会执行addCleanup()里添加的函数。
setUp()#在执行每个测试用例之前被执行，任何异常（除了unittest.SkipTest和AssertionError异常以外）都会当做是error而不是failure，且会终止当前测试用例的执行。
tearDown()#执行了setUp()方法后，不论测试用例执行是否成功，都执行tearDown()方法。如果tearDown()的代码有异常(除了unittest.SkipTest和AssertionError异常以外)，会多算一个error。
setUpClass( cls )与tearDownClass( cls )#测试用例们被执行前、后执行的方法，定义时必须加上classmethod装饰符
countTestCases()#返回测试用例的个数，对于TestCase实例来说，这个返回值一直是1.
defaultTestResult()#如果在run()方法中未提供result参数，该函数返回一个包含本用例测试结果的TestResult对象。
shortDescription()#返回测试用例的描述，即函数的docstring，如果没有，返回None。可以用于测试结果输出中描述测试内容。
id()#返回测试用例的编号，通常是如下格式：模块名.类名.函数名。可以用于测试结果的输出。
subTest( msg=_subtest_msg_sentinel, **params)#返回一个上下文管理器，它将返回由可选消息和关键字参数标识的子测试中的封闭代码块。子测试中的失败标志着测试用例失败，但在封闭块结束时恢复执行，允许执行进一步的测试代码。
run( result =None)#运行一个测试用例，将测试结果收集到result变量中，测试结果不返回给调用者。如果result参数的值为None，则测试结果在下面提到的defaultTestResult()方法的返回值中
doCleanups()#无条件强制调用addCleanup()添加的函数，适用于setUp()方法执行失败但是需要执行清理函数的场景，或者希望在tearDown()方法之前执行这些清理函数。
debug()#与run方法将测试结果存储到result变量中不同，debug方法运行测试用例将异常信息上报给调用者。
fail( msg =None)#无条件声明一个测试用例失败，msg是失败信息。
assertFalse( expr, msg=None) #检查表达式是否为假
assertTrue( expr, msg=None) #检查表达式是否为真
assertAlmostEqual与assertNotAlmostEqual(, first, second, places=None, msg=None,delta=None) #判断两个值是否约等于或者不约等于，places表示小数点后精确的位数
assertSequenceEqual(seq1, seq2, msg=None, seq_type=None) #有序序列的相等断言，如元组、列表
assertListEqual( list1, list2, msg=None) #列表相等的特定断言
assertTupleEqual(tuple1, tuple2, msg=None) #元组相等的特定断言
assertSetEqual( set1, set2, msg=None) #集合相等的特定断言
assertIn与assertNotIn( member, container, msg=None) #判断a 是否存在b中
assertIs与assertIsNot( expr1, expr2, msg=None) #判断a是不是b
assertDictEqual( d1, d2, msg=None) #检查两个字典是否相等
assertDictContainsSubset( subset, dictionary, msg=None) #检查字典是否是子集的超集。
assertCountEqual(first, second, msg=None) #判断两个无序列表内所出现的内容是否相等
assertMultiLineEqual( first, second, msg=None) #断言两个多行字符串相等
assertLess( a, b, msg=None) #断言a<b
assertLessEqual( a, b, msg=None) #断言a<=b
assertGreater( a, b, msg=None) #断言a>b
assertGreaterEqual(a, b, msg=None) #断言a>=b
assertIsNone与assertIsNotNone( obj, msg=None) #判断obj是否为空
assertIsInstance(a, b)与assertNotIsInstance(a, b)# 与assertTrue相同，其中的类型b，既可以是一个类型，也可以是类型组成的元组。
assertRaisesRegex( expected_exception, expected_regex,*args, **kwargs)#断言在引发异常中的消息与正则表达式匹配。
assertWarnsRegex( expected_warning, expected_regex,*args, **kwargs)#断言触发警告中的消息与ReGEXP匹配。基本功能类似于AdvestWr.NS.（）只有消息与正则表达式匹配的警告。被认为是成功的匹配
assertRegex与assertNotRegex(text, expected_regex, msg=None) #判断文本与正则表达式是否匹配
shortDescription()#返回测试用例的描述，即函数的docstring，如果没有，返回None。可以用于测试结果输出中描述测试内容。





